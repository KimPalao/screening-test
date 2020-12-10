from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Value

# Create your views here.


class Values(APIView):
    permission_classes = (permissions.AllowAny,)

    def put(self, request: Request):
        text = request.data.get("text")
        if not len(text.strip()):
            return Response({"message": "Text must not be empty"}, 422)
        if Value.objects.filter(text=text).exists():
            return Response({"message": "This value already exists"}, 409)
        value = Value.objects.create(text=text)
        return Response({"id": value.id}, 201)
