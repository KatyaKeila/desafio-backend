from django.urls import path

from . import views

urlpatterns = [
    path("form/", views.form_modelform, name="form_modelform"),
]
