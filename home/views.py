from rest_framework.views import APIView
from rest_framework.response import Response


class Home(APIView):
    def get(self, request):
        return Response({'name': 'amir'})

    def post(self, request):
        name = request.data['name']
        return Response({'name': name})
