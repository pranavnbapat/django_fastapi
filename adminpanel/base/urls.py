from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("upload-form/", views.upload_form, name="upload-form"),
    path("submit-upload-form/", views.submit_upload_form, name="submit-upload-form"),
]