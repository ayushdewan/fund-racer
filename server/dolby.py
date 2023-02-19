import requests

DOLBY_ID = 'Kb4XjT'
DOLBY_API_KEY = '273ab65417ee3a09f0cb2c03622a19e6319f8bee3a72f152ed1ffd0428515459'

import requests

def publish_token(name, label):
    url = "https://api.millicast.com/api/publish_token"

    payload = {
        "streams": [
            {
                "isRegex": False,
                "streamName": name
            }
        ],
        "subscribeRequiresAuth": False,
        "record": False,
        "multisource": False,
        "label": label
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {DOLBY_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
