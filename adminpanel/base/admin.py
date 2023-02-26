from django.contrib import admin

# Register your models here.
from .models import AdminMenuMaster
from .models import UploadFormModel

admin.site.register(AdminMenuMaster)
admin.site.register(UploadFormModel)
