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
    put_data: Dict
    patch_data: Dict

    def _get_single(self, request, id):
        object = self.view_model.objects.filter(pk=id).first()
        if not object:
            return Response({"message": f"{self.view_model.__name__} not found"}, 404)
        return Response({"data": object.to_json()})

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

        objects = objects.filter(**query_filter).order_by("pk")

        filtered_count = objects.count()

        objects = objects if "all" in request.query_params else objects.all()[start:end]

        data = [object.to_json() for object in objects]

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
        data = {}
        for field, meta in self.put_data.items():
            if meta.get("required", False) and field not in request.data:
                return Response({"message": f"{field.capitalize()} is required"}, 400)
            value = request.data.get(field)

            if not meta.get("blank", True) and not len(value.strip()):
                return Response(
                    {"message": f"{field.capitalize()} must not be empty"}, 422
                )
            if (
                meta.get("unique", False)
                and self.view_model.objects.filter(**{field: value}).exists()
            ):
                return Response(
                    {
                        "message": f"A {self.view_model.__name__} with this {field} already exists"
                    },
                    409,
                )
            data[field] = value

        object = self.view_model.objects.create(**data)
        return Response({"id": object.id}, 201)

    def patch(self, request: Request, id: int):
        q = self.view_model.objects.filter(pk=id)
        if not q.exists():
            return Response({"message": f"{self.view_model.__name__} not found"}, 404)

        data = {}

        for field, meta in self.patch_data.items():
            value = request.data.get(field, None)
            if value is not None:
                if (
                    meta.get("unique", False)
                    and self.view_model.objects.filter(**{field: value})
                    .exclude(pk=id)
                    .exists()
                ):
                    return Response(
                        {
                            "message": f"A {self.view_model.__name__} with this {field} already exists"
                        },
                        409,
                    )
                if not meta.get("blank", True) and not len(value.strip()):
                    return Response(
                        {"message": f"{field.capitalize()} must not be empty"}, 422
                    )
                data[field] = value
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

    put_data = {"text": {"required": True, "blank": False, "unique": True}}

    patch_data = {"text": {"blank": False, "unique": True}}


class Principles(CRUDView):
    view_model = Principle

    get_query_params = {
        "text_contains": "text__icontains",
    }

    put_data = {"text": {"required": True, "blank": False, "unique": True}}

    patch_data = {"text": {"blank": False, "unique": True}}