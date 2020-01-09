import json
import requests


def getUserToken():
    userID = '207b8e9fb0de47d180ea75049ab7b134'
    userSecret = '9135635ed042414587609c86fa4e88a6'

    grantType = 'client_credentials'

    bodyParams = {'grant_type': grantType}

    url = 'https://accounts.spotify.com/api/token'

    response = requests.post(url, data=bodyParams, auth=(userID, userSecret))

    tokenRaw = json.loads(response.text)

    return tokenRaw['access_token']

def renewToken(token):
    userID = '207b8e9fb0de47d180ea75049ab7b134'
    userSecret = '9135635ed042414587609c86fa4e88a6'

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
