from django.urls import path

from . import views

urlpatterns = [
    path("values", views.Values.as_view(), name="values"),
    path("values/<int:id>", views.Values.as_view(), name="values"),
    path("principles", views.Principles.as_view(), name="principles"),
    path("principles/<int:id>", views.Principles.as_view(), name="principles"),
]
