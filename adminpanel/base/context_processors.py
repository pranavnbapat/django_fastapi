from .models import AdminMenuMaster


def context_processors(req):
    admin_menu = AdminMenuMaster.objects.raw(
        "SELECT * FROM admin_menu_master WHERE status = 'a' ORDER BY menu_order ASC"
    )
    return {"admin_menu": admin_menu}

