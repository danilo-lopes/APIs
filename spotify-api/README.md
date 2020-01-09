# Structure

```
.
├── __main__.py
├── controller.py
└── list_user_playlist.py
```

## Flow

![Imgur](https://i.imgur.com/zg2yDlj.png)

## Controller

Responsable to get user [`Token`](https://auth0.com/docs/api-auth/why-use-access-tokens-to-secure-apis) session to allow us query tracks, artists and playlists of him.

Responsable for renew an old toker if it's necessary

## List User Playlist

And then, here we show informations like track name, track artist from user playlist
