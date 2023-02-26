from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import UploadFormModel
from .serializers import UploadFormSerializer


# Create your views here.
@api_view(['GET'])
def insert_upload_form(request):
    serializer = UploadFormSerializer(data=request.GET)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data saved successfully."}, status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
