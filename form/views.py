from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def form_modelform(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("form/form_modelform.html")

    else:
        form = UploadFileForm()
    return render(request, "form/form_modelform.html", {"form": form})
