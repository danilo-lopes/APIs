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

```
.
├── __main__.py
├── controller.py <---
└── list_user_playlist.py
```

Responsable to get user [`Token`](https://auth0.com/docs/api-auth/why-use-access-tokens-to-secure-apis) session to allow query tracks, artists and playlists of him.

Responsable for renew an old token if it's necessary.

## List User Playlist

```
.
├── __main__.py
├── controller.py
└── list_user_playlist.py  <---
```

Show information like track name and track artist from user playlist.
