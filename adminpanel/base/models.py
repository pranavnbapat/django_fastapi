from django.db import models
from django.core import validators


# Create your models here.
class AdminMenuMaster(models.Model):
    class Meta:
        db_table = "admin_menu_master"
        # verbose_name_plural = "admin_menu_master"
        # verbose_name = "admin_menu_master"

    menu_name = models.CharField(max_length=45, db_collation="utf8mb4_unicode_ci")
    menu_icon = models.CharField(max_length=45, db_collation="utf8mb4_unicode_ci")
    menu_order = models.PositiveIntegerField()
    menu_route = models.CharField(max_length=45, db_collation="utf8mb4_unicode_ci")

    def __str__(self):
        return self.menu_name, self.menu_icon, self.menu_order, self.menu_route


class UploadFormModel(models.Model):
    class Meta:
        db_table = "upload_form"

    name = models.CharField(max_length=50, db_collation="utf8mb4_unicode_ci")
    email = models.CharField(max_length=50, db_collation="utf8mb4_unicode_ci")
    password = models.CharField(max_length=100, db_collation="utf8mb4_unicode_ci")
    dob = models.DateField(max_length=12)
    gender = models.CharField(max_length=1, db_collation="utf8mb4_unicode_ci")
    url = models.CharField(max_length=200, db_collation="utf8mb4_unicode_ci")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, self.email, self.password, self.dob, self.gender, self.url

