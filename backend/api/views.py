from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Value

# Create your views here.


class Values(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request: Request):
        page = int(request.query_params.get("page", 1))
        per_page = int(request.query_params.get("per_page", 10))

        start = (page - 1) * per_page
        end = start + per_page

        objects = Value.objects

        filtered_count = objects.count()

        objects = objects if "all" in request.query_params else objects.all()[start:end]

        data = [{"id": object.id, "text": object.text} for object in objects]

        return Response(
            {
                "data": data,
                "filtered_count": filtered_count,
                "total_count": Value.objects.count(),
            }
        )

    def put(self, request: Request):
        text = request.data.get("text")
        if not len(text.strip()):
            return Response({"message": "Text must not be empty"}, 422)
        if Value.objects.filter(text=text).exists():
            return Response({"message": "This value already exists"}, 409)
        value = Value.objects.create(text=text)
        return Response({"id": value.id}, 201)
