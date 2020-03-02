import requests
import json

class authService:
    def __init__(self, userID, userSecret):
        self._userID = userID
        self._userSecret = userSecret
    
    def getToken(self):
        grantType = 'client_credentials'

        bodyParams = {'grant_type': grantType}

        url = 'https://accounts.spotify.com/api/token'

        response = requests.post(url, data=bodyParams, auth=(self._userID, self._userSecret))

        token = json.loads(response.text)

        return token['access_token']

    def validateToken(self, token):

        headers = {"Authorization": "Bearer {}".format(token)}

        userInfo = requests.get(
            url="https://api.spotify.com/v1/users/12144040557",
            headers=headers
        )

        return userInfo.reason
    
    def refreshToken(self, token):
        tokenValidity = self.validateToken(token)
        
        if tokenValidity == 'Unauthorized':
            grantType = 'client_credentials'

            bodyParams = {'grant_type': grantType, 'refresh_token': token}

            url = 'https://accounts.spotify.com/api/token'

            response = requests.post(url, data=bodyParams, auth=(self._userID, self._userSecret))

            token = json.loads(response.text)

            return token['access_token']
        
        else:
            return 'unable to refresh token'
