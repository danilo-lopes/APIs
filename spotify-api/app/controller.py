import json
import requests


def getUserToken():
    userID = ''
    userSecret = ''

    grantType = 'client_credentials'

    bodyParams = {'grant_type': grantType}

    url = 'https://accounts.spotify.com/api/token'

    response = requests.post(url, data=bodyParams, auth=(userID, userSecret))

    tokenRaw = json.loads(response.text)

    return tokenRaw['access_token']

def renewToken(token):
    userID = ''
    userSecret = ''

    grantType = 'client_credentials'

    bodyParams = {'grant_type': grantType, 'refresh_token': token}

    url = 'https://accounts.spotify.com/api/token'

    response = requests.post(url, data=bodyParams, auth=(userID, userSecret))

    newToken = json.loads(response.text)

    return newToken['access_token']

def haveControllerAcess(token):

    headers = {"Authorization": "Bearer {}".format(token)}

    userInfo = requests.get(
        url="https://api.spotify.com/v1/me",
        headers=headers
    )

    return userInfo.reason
