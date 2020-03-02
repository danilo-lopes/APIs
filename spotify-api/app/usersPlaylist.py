import requests
import json

class userPlaylist:
    def __init__(self, token):
        self._token = token
    
    def userSongs(self):

        headers = {"Authorization": "Bearer {}".format(self._token)}

        getPlaylists = requests.get(
            url="https://api.spotify.com/v1/users/12144040557/playlists",
            headers=headers
        )

        playlists = json.loads(getPlaylists.text)['items']

        for playlistInformation in playlists:
            albumID = playlistInformation['id']
            albumName = playlistInformation['name']
            albumIsPublic = playlistInformation['public']

            print(
                'Album ID: {}, Album Name: {}, Is Public?: {}'.format(
                    albumID, 
                    albumName, 
                    albumIsPublic
                )
            )

            getAlbumTracks = requests.get(
                url='https://api.spotify.com/v1/playlists/{}/tracks'.format(albumID),
                headers=headers
            )

            albumTracks = json.loads(getAlbumTracks.text)['items']

            for track in albumTracks:
                trackName = track['track']['name']
                
                for artistName in track['track']['artists']:
                    artist = artistName['name']

                    print('Track Name: {} - Artist: {}'.format(trackName, artist))
