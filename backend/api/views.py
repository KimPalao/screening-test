from typing import Dict
from django.db.models.base import Model
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Principle, Value

# Create your views here.


class CRUDView(APIView):
    view_model: Model

    permission_classes = (permissions.AllowAny,)

    get_query_params: Dict

    def _get_single(self, request, id):
        object = self.view_model.objects.filter(pk=id).first()
        if not object:
            return Response({"message": f"{self.view_model.__name__} not found"}, 404)
        return Response({"data": {"id": object.id, "text": object.text}})

    def _get_list(self, request):
        page = int(request.query_params.get("page", 1))
        per_page = int(request.query_params.get("per_page", 10))

        start = (page - 1) * per_page
        end = start + per_page

        objects = self.view_model.objects

        query_filter = {}

        for param, query in self.get_query_params.items():
            if param in request.query_params:
                query_filter[query] = request.query_params.get(param)

        objects = objects.filter(**query_filter)

        filtered_count = objects.count()

        objects = objects if "all" in request.query_params else objects.all()[start:end]

        data = [{"id": object.id, "text": object.text} for object in objects]

        return Response(
            {
                "data": data,
                "filtered_count": filtered_count,
                "total_count": self.view_model.objects.count(),
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
        if self.view_model.objects.filter(text=text).exists():
            return Response(
                {
                    "message": f"A {self.view_model.__name__} with this text already exists"
                },
                409,
            )
        object = self.view_model.objects.create(text=text)
        return Response({"id": object.id}, 201)

    def patch(self, request: Request, id: int):
        q = self.view_model.objects.filter(pk=id)
        if not q.exists():
            return Response({"message": f"{self.view_model.__name__} not found"}, 404)

        text = request.data.get("text", None)

        data = {}

        if text is not None:
            if self.view_model.objects.filter(text=text).exclude(pk=id).exists():
                return Response(
                    {
                        "message": f"A {self.view_model.__name__} with this text already exists"
                    },
                    409,
                )
            if not len(text.strip()):
                return Response({"message": "Text must not be empty"}, 422)
            data["text"] = text
        q.update(**data)
        return Response({}, 200)

    def delete(self, request: Request, id: int):
        object = self.view_model.objects.filter(pk=id).first()
        if not object:
            return Response({"message": f"{self.view_model.__name__} not found"}, 404)
        object.delete()
        return Response()


class Values(CRUDView):
    view_model = Value

    get_query_params = {
        "text_contains": "text__icontains",
    }


class Principles(CRUDView):
    view_model = Principle

    get_query_params = {
        "text_contains": "text__icontains",
    }
