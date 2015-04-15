from django.contrib import admin

# Register your models here.
from .models import Realserver, Realserver_Group_Permissions

class Realserver_Group_PermissionsAdmin(admin.ModelAdmin):
    list_display = ('realserver', 'group', 'allow_drain')

admin.site.register(Realserver)
admin.site.register(Realserver_Group_Permissions, Realserver_Group_PermissionsAdmin)