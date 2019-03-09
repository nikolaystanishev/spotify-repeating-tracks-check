from rest_framework.views import APIView
from rest_framework.response import Response


class PlaylistView(APIView):

    def get(self, request, username=None):
        return Response({'username': username})
