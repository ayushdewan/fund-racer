import requests

CHECKBOOK_HEADER = "0f05a177b3e94ef09e9228679483add9:kdWgiQjQYA6CCoFBmAOQxN1hYcOzeL"

def make_payment(amt, org, description=None):
    url = "https://sandbox.checkbook.io/v3/check/digital"

    payload = {
        "recipient": "testing@checkbook.io",
        "name": org,
        "amount": amt
    }
    
    if description is not None:
        payload["description"] = description

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": CHECKBOOK_HEADER
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
