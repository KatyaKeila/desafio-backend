from django.shortcuts import render
from rest_framework.views import APIView

from .forms import UploadFileForm


def form_modelform(request):
    if request.method == "GET":
        form = UploadFileForm()
        context = {
            "form": form,
        }

        return render(request, "form/form_modelform.html", context=context)

    else:
        form = UploadFileForm(request.POST)
        if form.is_valid():
            upload = form.save()
            form = UploadFileForm()

        context = {
            "form": form,
        }

        return render(request, "form/form_modelform.html", context=context)
