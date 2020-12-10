from django.urls import path

from . import views

urlpatterns = [path("values", views.Values.as_view(), name="values")]
