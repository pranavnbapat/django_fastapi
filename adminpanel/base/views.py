from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import UploadFormModel
from .forms import UploadForm
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(req):
    return render(req, "index.html")


def about(req):
    return render(req, "about.html")


def upload_form(req):
    # url = reverse_lazy("upload-form")
    # context = {"upload_form": url}
    return render(req, "upload-form.html")


def submit_upload_form(req):
    if req.method == "POST":
        form = UploadForm(req.POST)
        if form.is_valid():
            password = req.POST.get('password')
            hashed_password = make_password(password)

            upload_form = UploadFormModel()
            upload_form.name = form.cleaned_data['name']
            upload_form.email = form.cleaned_data['email']
            upload_form.password = hashed_password
            upload_form.dob = form.cleaned_data['dob']
            upload_form.url = form.cleaned_data['url']
            upload_form.gender = form.cleaned_data['gender']
            upload_form.save()
            return HttpResponse(200)
        else:
            error_list = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_list.append(f"{field}: {error}")
            error_str = "<br>".join(error_list)
            return HttpResponse(f"Errors in form:<br>{error_str}")
    else:
        return HttpResponse("Error")

    # if req.method == "POST":
    #     form = UploadForm(req.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse(200)

    # context = {"form": form}
    # return render(req, "upload-form", context)
