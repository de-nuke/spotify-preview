import json
import os
import re
from collections import defaultdict
from typing import Any, Dict, List, TypedDict, Union

import requests
from bs4 import BeautifulSoup

from utils import is_url, remove_query_params


class ValidationError(RuntimeError):
    pass


class NoDataError(RuntimeError):
    pass


SongData = TypedDict(
    "SongData",
    {"title": str, "description": str, "audio_url": str, "image_url": str, "url": str},
)
MetaProps = Dict[str, List[str]]
RequestType = Dict[str, Any]
ResponseType = TypedDict("ResponseType", {"statusCode": int, "headers": Dict[str, Any], "body": str})


def response(status_code: int, body: Any) -> ResponseType:
    return {
        "statusCode": int(status_code),
        "headers": {
            "Access-Control-Allow-Headers": os.environ.get("ACCESS_CONTROL_ALLOW_HEADERS", ""),
            "Access-Control-Allow-Origin": os.environ.get("ACCESS_CONTROL_ALLOW_ORIGIN", ""),
            "Access-Control-Allow-Methods": os.environ.get("ACCESS_CONTROL_ALLOW_METHODS", ""),
        },
        "body": body if isinstance(body, str) else json.dumps(body),
    }


def get_url(request: RequestType) -> str:
    try:
        return request["queryStringParameters"]["url"]
    except KeyError:
        return ""


def build_track_url(track_id: str) -> str:
    url_template = "https://open.spotify.com/track/{track_id}"
    return url_template.format(track_id=track_id)


def validate_spotify_url(url: str) -> str:
    """
    URL might be one of those:
    1. Spotify track URL (https://open.spotify.com/track/<track-id>)
    2. Spotify track URI (spotify:track:<track-id>)
    3. Track ID itself
    """
    if not url:
        raise ValidationError("'url' parameter required")

    url_regex = re.compile(r"^https?://" r"open\.spotify\.com/track/" r"(?P<track_id>[A-Za-z0-9]+)" r"/?\??\S*$")
    uri_regex = re.compile("^spotify:track:(?P<track_id>[A-Za-z0-9]+)$")
    track_id_regex = re.compile("^(?P<track_id>[A-Za-z0-9]+)$")

    for regex in [url_regex, uri_regex, track_id_regex]:
        match = regex.match(url)
        if match:
            return build_track_url(match.groupdict()["track_id"])

    raise ValidationError("Invalid track identifier. It must be URL, URI or ID")


def get_content(url: str) -> bytes:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.content


def get_meta_props(content: str) -> MetaProps:
    html = BeautifulSoup(content, features="html.parser")
    props = defaultdict(list)
    for tag in html.find_all("meta"):
        try:
            prop = tag["property"]
            content = tag["content"]
        except KeyError:
            pass
        else:
            if is_url(content):
                content = remove_query_params(content)
            props[prop].append(content)
    return props


def get_song_data(meta_props: MetaProps) -> SongData:
    def prep_value(value: Union[List[str], str]) -> str:
        if isinstance(value, list):
            if len(value) == 1:
                return value[0]
        return str(value)

    return {
        "title": prep_value(meta_props.get("og:title", "")),
        "description": prep_value(meta_props.get("og:description", "")),
        "audio_url": prep_value(meta_props.get("og:audio", "")),
        "image_url": prep_value(meta_props.get("og:image", "")),
        "url": prep_value(meta_props.get("og:url", "")),
    }


def get_response(request: RequestType) -> ResponseType:
    url = get_url(request)
    url = validate_spotify_url(url)
    content = get_content(url)
    meta_props = get_meta_props(content.decode("utf-8"))
    if not meta_props:
        raise NoDataError("Data not found in Spotify response")

    song_data = get_song_data(meta_props)

    return response(200, song_data)


def handle_error(error: Exception) -> ResponseType:
    error_body = {"detail": str(error)}
    return response(400, error_body)


def lambda_handler(event: RequestType, context: Any) -> ResponseType:
    try:
        return get_response(event)
    except (ValidationError, NoDataError) as e:
        return handle_error(e)
