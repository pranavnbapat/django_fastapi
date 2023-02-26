from django.forms import ModelForm
from .models import UploadFormModel


class UploadForm(ModelForm):
    class Meta:
        model = UploadFormModel
        fields = "__all__"

