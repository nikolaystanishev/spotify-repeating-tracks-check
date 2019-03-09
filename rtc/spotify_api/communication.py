from spotipy import Spotify, util


class SpotifyCommunication(object):

    def __init__(self, username, scope='playlist-read-private'):
        assert username

        token = util.prompt_for_user_token(username, scope)

        self.spotify = Spotify(auth=token)

    def get_user_playlists(self, username):
        assert username

        playlists = self.spotify.user_playlists(username)

        return playlists

    def get_user_playlists_names(self, username):
        playlists = self.get_user_playlists(username)

        return [playlist['name'] for playlist in playlists['items']]
