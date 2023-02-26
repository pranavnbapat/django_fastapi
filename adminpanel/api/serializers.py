from rest_framework import serializers
from base.models import UploadFormModel


class UploadFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFormModel
        fields = ("name", "email", "password", "url", "gender", "dob")
