from django.urls import path
from . import views

urlpatterns = [
    path('insert_upload_form/', views.insert_upload_form, name='insert_upload_form'),
]
