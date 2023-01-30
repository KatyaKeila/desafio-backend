from django import forms
from .models import Form


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ["title", "file"]
