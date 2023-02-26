from base.models import UploadFormModel


# from django.db import models
#
#
# # Create your models here.
# class UploadFormModel(models.Model):
#     class Meta:
#         db_table = "upload_form"
#
#     name = models.CharField(max_length=50, db_collation="utf8mb4_unicode_ci")
#     email = models.CharField(max_length=50, db_collation="utf8mb4_unicode_ci")
#     password = models.CharField(max_length=100, db_collation="utf8mb4_unicode_ci")
#     dob = models.DateField(max_length=12)
#     gender = models.CharField(max_length=1, db_collation="utf8mb4_unicode_ci")
#     url = models.CharField(max_length=200, db_collation="utf8mb4_unicode_ci")