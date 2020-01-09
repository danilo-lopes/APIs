import json
import requests


def printUserPlaylists(token):

    headers = {"Authorization": "Bearer {}".format(token)}

    getPlaylists = requests.get(
        url="https://api.spotify.com/v1/users/12144040557/playlists",
        headers=headers
    )

    userPlaylists = json.loads(getPlaylists.text)['items']

    for userPlaylistInformation in userPlaylists:
        albumID = userPlaylistInformation['id']
        albumName = userPlaylistInformation['name']
        albumIsPublic = userPlaylistInformation['public']

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

        userAlbumItems = json.loads(getAlbumTracks.text)['items']

        for userTrackInformation in userAlbumItems:
            trackName = userTrackInformation['track']['name']
            
            for userArtistTrack in userTrackInformation['track']['artists']:
                trackArtist = userArtistTrack['name']

                print('Track Name: {} - Artist: {}'.format(trackName, trackArtist))
