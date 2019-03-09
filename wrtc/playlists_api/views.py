from rest_framework.views import APIView
from rest_framework.response import Response

from spotify_api.communication import SpotifyCommunication


class PlaylistView(APIView):

    def get(self, request, username=None):
        self.spotify_communication = SpotifyCommunication(username)

        return Response({
            'playlists':
            self.spotify_communication.get_user_playlists_names(username)
        })
