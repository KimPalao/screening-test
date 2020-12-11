from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Value

# Create your views here.


class Values(APIView):
    permission_classes = (permissions.AllowAny,)

    def _get_single(self, request, id):
        object = Value.objects.filter(pk=id).first()
        if not object:
            return Response({}, 404)
        return Response({"data": {"id": object.id, "text": object.text}})

    def _get_list(self, request):
        page = int(request.query_params.get("page", 1))
        per_page = int(request.query_params.get("per_page", 10))

        start = (page - 1) * per_page
        end = start + per_page

        objects = Value.objects

        if "text_contains" in request.query_params:
            objects = objects.filter(
                text__icontains=request.query_params.get("text_contains")
            )

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

    def get(self, request: Request, id=0):
        if id:
            return self._get_single(request, id)
        return self._get_list(request)

    def put(self, request: Request):
        if "text" not in request.data:
            return Response({"message": "Text is required"}, 400)
        text = request.data.get("text")
        if not len(text.strip()):
            return Response({"message": "Text must not be empty"}, 422)
        if Value.objects.filter(text=text).exists():
            return Response({"message": "This value already exists"}, 409)
        value = Value.objects.create(text=text)
        return Response({"id": value.id}, 201)
