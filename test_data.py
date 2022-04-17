from typing import Any, Dict

API_GATEWAY_EVENT: Dict[str, Any] = {
    "resource": "/preview",
    "path": "/preview",
    "httpMethod": "GET",
    "headers": None,
    "multiValueHeaders": None,
    "queryStringParameters": {"url": None},
    "multiValueQueryStringParameters": {"url": [None]},
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "6t8xv7",
        "resourcePath": "/preview",
        "httpMethod": "GET",
        "extendedRequestId": "PU3u-HCEFiAFZPg=",
        "requestTime": "21/Mar/2022:08:38:42 +0000",
        "path": "/preview",
        "accountId": "359988466181",
        "protocol": "HTTP/1.1",
        "stage": "test-invoke-stage",
        "domainPrefix": "testPrefix",
        "requestTimeEpoch": 1647851922868,
        "requestId": "5ff0b112-9058-446c-a84e-4c36f2b272ce",
        "identity": {
            "cognitoIdentityPoolId": None,
            "cognitoIdentityId": None,
            "apiKey": "test-invoke-api-key",
            "principalOrgId": None,
            "cognitoAuthenticationType": None,
            "userArn": "arn:aws:iam::359988466181:root",
            "apiKeyId": "test-invoke-api-key-id",
            "userAgent": (
                "aws-internal/3 aws-sdk-java/1.12.162 Linux/5.4.176-103.347.amzn2int.x86_64 "
                "OpenJDK_64-Bit_Server_VM/25.322-b06 java/1.8.0_322 vendor/Oracle_Corporation cfg/retry-mode/standard"
            ),
            "accountId": "359988466181",
            "caller": "359988466181",
            "sourceIp": "test-invoke-source-ip",
            "accessKey": "ASIAVHUH4CIC7R4GSY65",
            "cognitoAuthenticationProvider": None,
            "user": "359988466181",
        },
        "domainName": "testPrefix.testDomainName",
        "apiId": "cl5qtr94ti",
    },
    "body": None,
    "isBase64Encoded": False,
}


SPOTIFY_TRACK_HTML_CONTENT = """
<!DOCTYPE html>
<html lang=pl dir="ltr" class="">
<head>
    <meta charset="UTF-8">
    <title>Nothing is Safe - song by clipping. | Spotify</title>
    <meta name="description" content="Listen to Nothing is Safe on Spotify. clipping. · Song · 2019."/>
    <meta property="google" content="notranslate"/>
    <meta property="fb:app_id" content="174829003346"/>
    <meta property="og:title" content="Nothing is Safe"/>
    <meta property="og:description" content="clipping. · Song · 2019"/>
    <meta property="og:url" content="https://open.spotify.com/track/52UthFOfrbtnjBMK6jyLqk"/>
    <meta property="og:image" content="https://i.scdn.co/image/ab67616d0000b2734d1c35edb0aafeb16ef7c7df"/>
    <meta property="og:type" content="music.song"/>
    <meta property="og:site_name" content="Spotify"/>
    <meta property="og:restrictions:country:allowed" content="AD"/>
    <meta property="og:restrictions:country:allowed" content="AE"/>
    <meta property="og:restrictions:country:allowed" content="AG"/>
    <meta property="og:restrictions:country:allowed" content="AL"/>

    <meta property="og:audio"
          content="https://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57?cid=162b7dc01f3a4a2ca32ed3cec83d1e02&amp;utm_medium=facebook"/>
    <meta property="og:audio:type" content="audio/vnd.facebook.bridge"/>
    <meta property="music:preview_url:url"
          content="http://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"/>
    <meta property="music:preview_url:secure_url"
          content="https://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"/>
    <meta property="music:preview_url:type" content="audio/mpeg"/>
    <meta property="music:musician" content="https://open.spotify.com/artist/5HJ2kX5UTwN4Ns8fB5Rn1I"/>
    <meta property="music:duration" content="297"/>
    <meta property="music:album" content="https://open.spotify.com/album/0xeEJgJP2Mkyr3dMKbCQP3"/>
    <meta property="music:album:track" content="2"/>
    <meta property="music:release_date" content="2019-10-18"/>
    <meta property="al:android:app_name" content="Spotify"/>
    <meta property="al:android:package" content="com.spotify.music"/>
    <meta property="al:android:url" content="spotify://track/52UthFOfrbtnjBMK6jyLqk?si=fc856f0a4f2a4f6b&amp;nd=1"/>
    <meta property="al:ios:app_name" content="Spotify"/>
    <meta property="al:ios:app_store_id" content="324684580"/>
    <meta property="al:ios:url" content="spotify://track/52UthFOfrbtnjBMK6jyLqk?si=fc856f0a4f2a4f6b&amp;nd=1"/>
    <meta property="twitter:site" content="@spotify"/>
    <meta property="twitter:title" content="Nothing is Safe"/>
    <meta property="twitter:description" content="clipping. · Song · 2019"/>
    <meta property="twitter:image" content="https://i.scdn.co/image/ab67616d0000b2734d1c35edb0aafeb16ef7c7df"/>
    <meta property="twitter:card" content="summary"/>
    <meta name="robots" content="noindex"/>
    <link rel="canonical" href="https://open.spotify.com/track/52UthFOfrbtnjBMK6jyLqk"/>
    <link rel="alternate" type="application/json+oembed"
          href="https://open.spotify.com/oembed?url=https%3A%2F%2Fopen.spotify.com%2Ftrack%2F52UthFOfrbtnjBMK6jyLqk"/>
    <link rel="alternate"
          href="android-app://com.spotify.music/spotify/track/52UthFOfrbtnjBMK6jyLqk?si=fc856f0a4f2a4f6b&amp;nd=1"/>
    <script type="application/ld+json"></script>
    <link rel="icon" sizes="32x32" type="image/png" href="https://open.scdn.co/cdn/images/favicon32.8e66b099.png"/>
    <link rel="icon" sizes="16x16" type="image/png" href="https://open.scdn.co/cdn/images/favicon16.c498a969.png"/>
    <link rel="icon" href="https://open.scdn.co/cdn/images/favicon.5cb2bd30.ico">
    <link rel="manifest" href="https://open.scdn.co/cdn/generated/manifest-web-player.562e545c.json">
    <link rel="stylesheet" href="https://open.scdn.co/cdn/build/web-player/web-player.e836238b.css"/>
    <script id="config" data-testid="config" type="application/json">{}</script>
    <script id="baba" type="application/json">[]</script>
    <script defer src="https://www.googleoptimize.com/optimize.js?id=GTM-W53X654"></script>
    <script defer src="https://open.scdn.co/cdn/js/gtm.7dc32ad7.js"></script>
    <link rel="preconnect" href="https://api.spotify.com" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Book.3466e0ec.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Bold.8d0a45cc.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Light.afd9ab26.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <style>.grecaptcha-badge {
        display: none !important;
    }</style>
    <script src="https://www.google.com/recaptcha/enterprise.js?render=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39" async
            defer></script>
    <link rel="search" type="application/opensearchdescription+xml" title="Spotify"
          href="https://open.scdn.co/cdn/generated/opensearch.7e787b90.xml"/>
</head>
<body class="" data-locale="pl" data-market="PL">
    <div class="body-drag-top"></div>
    <script id="jsonTranslations" type="application/json" data-locale="pl">{}</script>
    <script id="seo" type="application/json">{}</script>
    <script type="text/plain" id="remote-configuration">
        eyIjdiI6IjEiLCJlbmFibGVNdWx0aVZpc2l0IjoiY29udHJvbCIsImVuYWJsZUludGVybmFsVHJhY2tMaW5rcyI6ImNvbnRyb2wiLCJlbmFibGVOZXdQbGF5bGlzdENyZWF0aW9uIjp0cnVlLCJlbmFibGVVc2VyUHJvZmlsZUVkaXQiOnRydWUsImVuYWJsZUNsaWVudFhDb25jZXJ0c0h1YiI6dHJ1ZSwiZW5hYmxlQ2xpZW50WENvbmNlcnRzRm9yQXJ0aXN0UGFnZSI6dHJ1ZSwicG9kY2FzdE1ldGFkYXRhU291cmNlIjoiUEFUSEZJTkRFUiIsImVuYWJsZVNvdW5kYmV0dGVyU29jaWFsTGluayI6dHJ1ZSwiZW5hYmxlU3VidGl0bGVzVXNpbmdIYXJtb255Ijp0cnVlLCJlbmFibGVTdWJ0aXRsZXNBdXRvZ2VuZXJhdGVkTGFiZWwiOnRydWUsImVuYWJsZUhUTUxEZXNjcmlwdGlvbnMiOnRydWUsImVuYWJsZUFydGlzdExpa2VkU29uZ3MiOnRydWUsImVuYWJsZUJsb2NrVXNlcnMiOnRydWUsImVuYWJsZUx5cmljc0ZlYXR1cmVDbGllbnRTaWRlIjp0cnVlLCJlbmFibGVDb3ZpZEh1YkJhbm5lciI6dHJ1ZSwiZW5hYmxlQ29udGVudEluZm9ybWF0aW9uTWVzc2FnZSI6dHJ1ZSwiZW5hYmxlU2VhcmNoTW9kYWwiOnRydWUsImVuYWJsZVVyaUxpbmtzIjp0cnVlLCJlbmFibGVCbGVuZEludml0YXRpb24iOiJNVUxUSV9VU0VSIiwiI2NvbmZpZ3VyYXRpb25Bc3NpZ25tZW50SWQiOiJkMDYwYjc1Zi0zODNiLWYyZDQtNTU3Ni0xOTliOTZiODE1MmMiLCIjZ3JvdXBJZHMiOnsiZW5hYmxlTXVsdGlWaXNpdCI6MTAzOTUwNywiZW5hYmxlSW50ZXJuYWxUcmFja0xpbmtzIjoxMDQxODQwLCJlbmFibGVJbmxpbmVDdXJhdGlvbiI6MzI4NDEsImVuYWJsZU5ld1BsYXlsaXN0Q3JlYXRpb24iOjMwMzE0LCJlbmFibGVVc2VyUHJvZmlsZUVkaXQiOjMzNDMyLCJlbmFibGVDbGllbnRYQ29uY2VydHNIdWIiOjM0MDU1LCJlbmFibGVDbGllbnRYQ29uY2VydHNGb3JBcnRpc3RQYWdlIjozNDcwNSwicG9kY2FzdE1ldGFkYXRhU291cmNlIjo4NTQ2LCJlbmFibGVTb3VuZGJldHRlclNvY2lhbExpbmsiOjM0OTc3LCJlbmFibGVTdWJ0aXRsZXNVc2luZ0hhcm1vbnkiOjM1NTE5LCJlbmFibGVTdWJ0aXRsZXNBdXRvZ2VuZXJhdGVkTGFiZWwiOjM1Nzc1LCJlbmFibGVJbmxpbmVDdXJhdGlvbkRlc2t0b3AiOjMzMTU5MywiZW5hYmxlSFRNTERlc2NyaXB0aW9ucyI6MTAwMjYwNiwiZW5hYmxlQXJ0aXN0TGlrZWRTb25ncyI6MTAwMjQ3NCwiZW5hYmxlTXVzaWNBbmRUYWxrIjoxMDA4NTA5LCJlbmFibGVCbG9ja1VzZXJzIjoxMDIxNTI0LCJlbmFibGVMeXJpY3NGZWF0dXJlQ2xpZW50U2lkZSI6MTAyNzExMSwiZW5hYmxlRW5jb3JlV2ViTWlncmF0aW9uIjoxMDI5NjEyLCJlbmFibGVJY29uc1JlZHJhdyI6MTAyMjI3MCwiZW5hYmxlQ292aWRIdWJCYW5uZXIiOjEwMzUwNjMsImVuYWJsZUNvbnRlbnRJbmZvcm1hdGlvbk1lc3NhZ2UiOjEwMzUxNzQsImVuYWJsZVNlYXJjaE1vZGFsIjoxMDM1MzE3LCJlbmFibGVVcmlMaW5rcyI6MTAzNjA2OSwiZW5hYmxlQmxlbmRJbnZpdGF0aW9uIjoxMDM2MDY5fSwiI2ZldGNoVGltZU1pbGxpcyI6MTY0Nzk0NDE3NDUwOSwiI2NvbnRleHRIYXNoIjoiNWMxMmQ1NWMzMjJhMjkzNCJ9

    </script>
    <script src="https://open.scdn.co/cdn/build/web-player/web-player.79f63296.js"></script>
    <script src="https://open.scdn.co/cdn/build/web-player/vendor~web-player.8ab8967f.js"></script>
</body>
</html>
"""


EXPECTED_META_PROPS = {
    "google": ["notranslate"],
    "fb:app_id": ["174829003346"],
    "og:title": ["Nothing is Safe"],
    "og:description": ["clipping. · Song · 2019"],
    "og:url": ["https://open.spotify.com/track/52UthFOfrbtnjBMK6jyLqk"],
    "og:image": ["https://i.scdn.co/image/ab67616d0000b2734d1c35edb0aafeb16ef7c7df"],
    "og:type": ["music.song"],
    "og:site_name": ["Spotify"],
    "og:restrictions:country:allowed": ["AD", "AE", "AG", "AL"],
    "og:audio": ["https://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57"],
    "og:audio:type": ["audio/vnd.facebook.bridge"],
    "music:preview_url:url": ["http://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57"],
    "music:preview_url:secure_url": ["https://p.scdn.co/mp3-preview/78868f138472a9b6ba194fefafb536a7b017fc57"],
    "music:preview_url:type": ["audio/mpeg"],
    "music:musician": ["https://open.spotify.com/artist/5HJ2kX5UTwN4Ns8fB5Rn1I"],
    "music:duration": ["297"],
    "music:album": ["https://open.spotify.com/album/0xeEJgJP2Mkyr3dMKbCQP3"],
    "music:album:track": ["2"],
    "music:release_date": ["2019-10-18"],
    "al:android:app_name": ["Spotify"],
    "al:android:package": ["com.spotify.music"],
    "al:android:url": ["spotify://track/52UthFOfrbtnjBMK6jyLqk"],
    "al:ios:app_name": ["Spotify"],
    "al:ios:app_store_id": ["324684580"],
    "al:ios:url": ["spotify://track/52UthFOfrbtnjBMK6jyLqk"],
    "twitter:site": ["@spotify"],
    "twitter:title": ["Nothing is Safe"],
    "twitter:description": ["clipping. · Song · 2019"],
    "twitter:image": ["https://i.scdn.co/image/ab67616d0000b2734d1c35edb0aafeb16ef7c7df"],
    "twitter:card": ["summary"],
}

SPOTIFY_TRACK_HTML_CONTENT_WITHOUT_META = """
<!DOCTYPE html>
<html lang=pl dir="ltr" class="">
<head>
    <meta charset="UTF-8">
    <title>Nothing is Safe - song by clipping. | Spotify</title>
    <meta name="description" content="Listen to Nothing is Safe on Spotify. clipping. · Song · 2019."/>
    <meta name="robots" content="noindex"/>
    <link rel="canonical" href="https://open.spotify.com/track/52UthFOfrbtnjBMK6jyLqk"/>
    <link rel="alternate" type="application/json+oembed"
          href="https://open.spotify.com/oembed?url=https%3A%2F%2Fopen.spotify.com%2Ftrack%2F52UthFOfrbtnjBMK6jyLqk"/>
    <link rel="alternate"
          href="android-app://com.spotify.music/spotify/track/52UthFOfrbtnjBMK6jyLqk?si=fc856f0a4f2a4f6b&amp;nd=1"/>
    <script type="application/ld+json"></script>
    <link rel="icon" sizes="32x32" type="image/png" href="https://open.scdn.co/cdn/images/favicon32.8e66b099.png"/>
    <link rel="icon" sizes="16x16" type="image/png" href="https://open.scdn.co/cdn/images/favicon16.c498a969.png"/>
    <link rel="icon" href="https://open.scdn.co/cdn/images/favicon.5cb2bd30.ico">
    <link rel="manifest" href="https://open.scdn.co/cdn/generated/manifest-web-player.562e545c.json">
    <link rel="stylesheet" href="https://open.scdn.co/cdn/build/web-player/web-player.e836238b.css"/>
    <script id="config" data-testid="config" type="application/json">{}</script>
    <script id="baba" type="application/json">[]</script>
    <script defer src="https://www.googleoptimize.com/optimize.js?id=GTM-W53X654"></script>
    <script defer src="https://open.scdn.co/cdn/js/gtm.7dc32ad7.js"></script>
    <link rel="preconnect" href="https://api.spotify.com" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Book.3466e0ec.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Bold.8d0a45cc.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <link rel="preload" href="https://open.scdn.co/cdn/fonts/CircularSpUIv3T-Light.afd9ab26.woff2" as="font"
          type="font/woff2" crossorigin="anonymous">
    <style>.grecaptcha-badge {
        display: none !important;
    }</style>
    <script src="https://www.google.com/recaptcha/enterprise.js?render=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39" async
            defer></script>
    <link rel="search" type="application/opensearchdescription+xml" title="Spotify"
          href="https://open.scdn.co/cdn/generated/opensearch.7e787b90.xml"/>
</head>
<body class="" data-locale="pl" data-market="PL">
    <div class="body-drag-top"></div>
    <script id="jsonTranslations" type="application/json" data-locale="pl">{}</script>
    <script id="seo" type="application/json">{}</script>
    <script type="text/plain" id="remote-configuration">
        eyIjdiI6IjEiLCJlbmFibGVNdWx0aVZpc2l0IjoiY29udHJvbCIsImVuYWJsZUludGVybmFsVHJhY2tMaW5rcyI6ImNvbnRyb2wiLCJlbmFibGVOZXdQbGF5bGlzdENyZWF0aW9uIjp0cnVlLCJlbmFibGVVc2VyUHJvZmlsZUVkaXQiOnRydWUsImVuYWJsZUNsaWVudFhDb25jZXJ0c0h1YiI6dHJ1ZSwiZW5hYmxlQ2xpZW50WENvbmNlcnRzRm9yQXJ0aXN0UGFnZSI6dHJ1ZSwicG9kY2FzdE1ldGFkYXRhU291cmNlIjoiUEFUSEZJTkRFUiIsImVuYWJsZVNvdW5kYmV0dGVyU29jaWFsTGluayI6dHJ1ZSwiZW5hYmxlU3VidGl0bGVzVXNpbmdIYXJtb255Ijp0cnVlLCJlbmFibGVTdWJ0aXRsZXNBdXRvZ2VuZXJhdGVkTGFiZWwiOnRydWUsImVuYWJsZUhUTUxEZXNjcmlwdGlvbnMiOnRydWUsImVuYWJsZUFydGlzdExpa2VkU29uZ3MiOnRydWUsImVuYWJsZUJsb2NrVXNlcnMiOnRydWUsImVuYWJsZUx5cmljc0ZlYXR1cmVDbGllbnRTaWRlIjp0cnVlLCJlbmFibGVDb3ZpZEh1YkJhbm5lciI6dHJ1ZSwiZW5hYmxlQ29udGVudEluZm9ybWF0aW9uTWVzc2FnZSI6dHJ1ZSwiZW5hYmxlU2VhcmNoTW9kYWwiOnRydWUsImVuYWJsZVVyaUxpbmtzIjp0cnVlLCJlbmFibGVCbGVuZEludml0YXRpb24iOiJNVUxUSV9VU0VSIiwiI2NvbmZpZ3VyYXRpb25Bc3NpZ25tZW50SWQiOiJkMDYwYjc1Zi0zODNiLWYyZDQtNTU3Ni0xOTliOTZiODE1MmMiLCIjZ3JvdXBJZHMiOnsiZW5hYmxlTXVsdGlWaXNpdCI6MTAzOTUwNywiZW5hYmxlSW50ZXJuYWxUcmFja0xpbmtzIjoxMDQxODQwLCJlbmFibGVJbmxpbmVDdXJhdGlvbiI6MzI4NDEsImVuYWJsZU5ld1BsYXlsaXN0Q3JlYXRpb24iOjMwMzE0LCJlbmFibGVVc2VyUHJvZmlsZUVkaXQiOjMzNDMyLCJlbmFibGVDbGllbnRYQ29uY2VydHNIdWIiOjM0MDU1LCJlbmFibGVDbGllbnRYQ29uY2VydHNGb3JBcnRpc3RQYWdlIjozNDcwNSwicG9kY2FzdE1ldGFkYXRhU291cmNlIjo4NTQ2LCJlbmFibGVTb3VuZGJldHRlclNvY2lhbExpbmsiOjM0OTc3LCJlbmFibGVTdWJ0aXRsZXNVc2luZ0hhcm1vbnkiOjM1NTE5LCJlbmFibGVTdWJ0aXRsZXNBdXRvZ2VuZXJhdGVkTGFiZWwiOjM1Nzc1LCJlbmFibGVJbmxpbmVDdXJhdGlvbkRlc2t0b3AiOjMzMTU5MywiZW5hYmxlSFRNTERlc2NyaXB0aW9ucyI6MTAwMjYwNiwiZW5hYmxlQXJ0aXN0TGlrZWRTb25ncyI6MTAwMjQ3NCwiZW5hYmxlTXVzaWNBbmRUYWxrIjoxMDA4NTA5LCJlbmFibGVCbG9ja1VzZXJzIjoxMDIxNTI0LCJlbmFibGVMeXJpY3NGZWF0dXJlQ2xpZW50U2lkZSI6MTAyNzExMSwiZW5hYmxlRW5jb3JlV2ViTWlncmF0aW9uIjoxMDI5NjEyLCJlbmFibGVJY29uc1JlZHJhdyI6MTAyMjI3MCwiZW5hYmxlQ292aWRIdWJCYW5uZXIiOjEwMzUwNjMsImVuYWJsZUNvbnRlbnRJbmZvcm1hdGlvbk1lc3NhZ2UiOjEwMzUxNzQsImVuYWJsZVNlYXJjaE1vZGFsIjoxMDM1MzE3LCJlbmFibGVVcmlMaW5rcyI6MTAzNjA2OSwiZW5hYmxlQmxlbmRJbnZpdGF0aW9uIjoxMDM2MDY5fSwiI2ZldGNoVGltZU1pbGxpcyI6MTY0Nzk0NDE3NDUwOSwiI2NvbnRleHRIYXNoIjoiNWMxMmQ1NWMzMjJhMjkzNCJ9

    </script>
    <script src="https://open.scdn.co/cdn/build/web-player/web-player.79f63296.js"></script>
    <script src="https://open.scdn.co/cdn/build/web-player/vendor~web-player.8ab8967f.js"></script>
</body>
</html>
"""
