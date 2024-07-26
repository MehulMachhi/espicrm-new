
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(AdminSite):
    site_header = _("Custom Admin")
    site_title = _("Custom Admin Portal")
    index_title = _("Welcome to Custom Admin")

custom_admin_site = CustomAdminSite(name='custom_admin')