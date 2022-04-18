import json
import unittest
from copy import deepcopy
from typing import Any, Dict
from unittest import mock
from unittest.mock import MagicMock

from requests import Response

from main import (NoDataError, ValidationError, build_track_url,
                  get_meta_props, get_response, get_song_data, get_url,
                  handle_error, lambda_handler, validate_spotify_url)
from test_data import (API_GATEWAY_EVENT, EXPECTED_META_PROPS,
                       SPOTIFY_TRACK_HTML_CONTENT,
                       SPOTIFY_TRACK_HTML_CONTENT_WITHOUT_META)


def make_api_gateway_event(url: str) -> Dict[str, Any]:
    event = deepcopy(API_GATEWAY_EVENT)
    event["queryStringParameters"]["url"] = url
    event["multiValueQueryStringParameters"]["url"] = [url]
    return event


def raise_error(error: Exception):
    raise error


class TestValidateSpotifyUrl(unittest.TestCase):
    """Test :py:func:`main.validate_spotify_url`"""

    def test_valid(self) -> None:
        track_id = "1UUBkjBgce8P53hQC3nHtU"
        valid_identifiers = [
            f"https://open.spotify.com/track/{track_id}?si=76e0e46d5d7742e0",
            f"https://open.spotify.com/track/{track_id}?si=",
            f"http://open.spotify.com/track/{track_id}?si",
            f"https://open.spotify.com/track/{track_id}?",
            f"https://open.spotify.com/track/{track_id}",
            f"http://open.spotify.com/track/{track_id}/",
            f"spotify:track:{track_id}",
            track_id,
        ]
        for identifier in valid_identifiers:
            with self.subTest(identifier=identifier):
                url = validate_spotify_url(identifier)
                self.assertEqual(url, f"https://open.spotify.com/track/{track_id}")

    def test_invalid(self) -> None:
        track_id = "1UUBkjBgce8P53hQC3nHtU"
        invalid_identifiers = [
            f"htt://open.spotify.com/track/{track_id}?si=76e0e46d5d7742e0",
            f"https:/open.spotify.com/track/{track_id}?si=",
            f"https://spotify.com/track/{track_id}?si",
            f"https://open.spotify.com/{track_id}?",
            "https://open.spotify.com/track/",
            "https://open.spotify.com/track?si=76e0e46d5d7742e0",
            f"track:{track_id}",
            track_id + "/",
        ]
        for identifier in invalid_identifiers:
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValidationError):
                    validate_spotify_url(identifier)


class TestBuildTrackUrl(unittest.TestCase):
    """Test :py:func:'main.build_track_url'"""

    def test_build(self) -> None:
        url = build_track_url("1UUBkjBgce8P53hQC3nHtU")
        self.assertEqual(url, "https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")


class TestGetUrl(unittest.TestCase):
    """Test :py:func:'main.get_url'"""

    def test_url_exists(self) -> None:
        event = make_api_gateway_event("https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")
        url = get_url(event)
        self.assertEqual(url, "https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")

    def test_url_missing(self) -> None:
        event = deepcopy(API_GATEWAY_EVENT)
        del event["queryStringParameters"]["url"]
        url = get_url(event)
        self.assertEqual(url, "")

    def test_query_params_missing(self) -> None:
        event = deepcopy(API_GATEWAY_EVENT)
        del event["queryStringParameters"]
        url = get_url(event)
        self.assertEqual(url, "")


class TestGetMeta(unittest.TestCase):
    """Test :py:func:`main.get_metadata`"""

    def test_valid_html(self) -> None:
        meta_props = get_meta_props(SPOTIFY_TRACK_HTML_CONTENT)
        self.assertEqual(meta_props, EXPECTED_META_PROPS)

    def test_valid_html_without_meta(self) -> None:
        meta_props = get_meta_props(SPOTIFY_TRACK_HTML_CONTENT_WITHOUT_META)
        self.assertEqual(meta_props, {})

    def test_invalid_html(self) -> None:
        meta_props = get_meta_props("This is not a valid HTML")
        self.assertEqual(meta_props, {})


class TestGetSongData(unittest.TestCase):
    """Test :py:func:`main.get_song_data`"""

    def test_full_props(self) -> None:
        song_data = get_song_data(EXPECTED_META_PROPS)
        expected_song_data = {
            "title": "Nothing is Safe",
            "description": "clipping. · Song · 2019",
            "audio_url": "https://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57",
            "image_url": "https://i.scdn.co/image/ab67616d0000b2734d1c35edb0aafeb16ef7c7df",
            "url": "https://open.spotify.com/track/52UthFOfrbtnjBMK6jyLqk",
        }
        self.assertEqual(song_data, expected_song_data)

    def test_empty_props(self) -> None:
        song_data = get_song_data({})
        expected_song_data = {
            "title": "",
            "description": "",
            "audio_url": "",
            "image_url": "",
            "url": "",
        }
        self.assertEqual(song_data, expected_song_data)


class TestGetResponse(unittest.TestCase):
    """Test :py:func:`main.get_response`"""

    def test_get_response_successfully(self) -> None:
        request = make_api_gateway_event("https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")
        mock_response = MagicMock(content=b'<meta property="og:title" content="Nothing is Safe"/>')
        with mock.patch("requests.get", return_value=mock_response):
            response = get_response(request)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        self.assertEqual(response["statusCode"], 200)

    def test_get_response_no_data_in_content(self) -> None:
        request = make_api_gateway_event("https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")
        with mock.patch("requests.get", return_value=MagicMock(content=b"")):
            with self.assertRaises(NoDataError):
                get_response(request)

    @mock.patch("main.get_url")
    @mock.patch("main.validate_spotify_url")
    @mock.patch("main.get_content")
    @mock.patch("main.get_meta_props")
    @mock.patch("main.get_song_data")
    @mock.patch("main.json.dumps")
    def test_get_response_all_calls_in_order(
        self,
        mock_json_dumps,
        mock_get_song_data,
        mock_get_meta_props,
        mock_get_content,
        mock_validate_spotify_url,
        mock_get_url,
    ) -> None:
        request = make_api_gateway_event("ABC")
        get_response(request)

        mock_get_url.assert_called_with(request)
        mock_validate_spotify_url.assert_called_with(mock_get_url.return_value)
        mock_get_content.assert_called_with(mock_validate_spotify_url.return_value)
        mock_get_meta_props.assert_called_with(mock_get_content.return_value.decode.return_value)
        mock_get_song_data.assert_called_with(mock_get_meta_props.return_value)
        mock_json_dumps.assert_called_with(mock_get_song_data.return_value)


class TestHandleError(unittest.TestCase):
    def test(self) -> None:
        error = ValidationError("Error")
        ret_val = handle_error(error)
        self.assertEqual(
            ret_val,
            {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,GET",
                },
                "body": json.dumps({"detail": "Error"}),
            },
        )


class TestLambdaHandler(unittest.TestCase):
    @mock.patch("requests.get")
    def test_success(self, mocked_get) -> None:
        # Mocking requests
        response_mock = Response()
        response_mock.status_code = 200
        response_mock._content = SPOTIFY_TRACK_HTML_CONTENT.encode("utf-8")
        mocked_get.return_value = response_mock

        event = make_api_gateway_event("https://open.spotify.com/track/1UUBkjBgce8P53hQC3nHtU")
        response = lambda_handler(event, {})
        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        self.assertEqual(response["statusCode"], 200)

    def test_error(self) -> None:
        errors = [ValidationError("Error message"), NoDataError("Error message")]
        for error in errors:
            with self.subTest(error=error.__class__.__name__):
                with mock.patch(
                    "main.get_response",
                    side_effect=lambda *args, **kwargs: raise_error(error),
                ):
                    response = lambda_handler(mock.MagicMock(), {})
                self.assertIsInstance(response, dict)
                self.assertIn("statusCode", response)
                self.assertIn("body", response)
                self.assertEqual(response["statusCode"], 400)
                self.assertEqual(response["body"], json.dumps({"detail": "Error message"}))

    def test_no_url_error(self) -> None:
        event = make_api_gateway_event(None)  # type: ignore
        response = lambda_handler(event, {})
        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        self.assertEqual(400, response["statusCode"])


if __name__ == "__main__":
    unittest.main()
