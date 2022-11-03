from django.db import connection
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LivenessProbe(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response("ok")


class ReadnessProbe(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            row = cursor.fetchone()
        return Response("ok")
