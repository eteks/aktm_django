from django.contrib import admin
from .models import UserPermission, SuperAdminusers, Adminusers, Managerusers
# Register your models here.
class UserPermissionAdmin(admin.ModelAdmin):
    model = UserPermission
    list_display = ('user_type',
                    'can_add_admin',
                    'can_edit_admin',
                    'can_delete_admin',
                    'can_viewlog_admin',
                    'can_add_manager',
                    'can_edit_manager',
                    'can_delete_manager',
                    'can_viewlog_manager',
                    'can_add_employee',
                    'can_edit_employee',
                    'can_delete_employee',
                    'can_viewlog_employee'
                    )

class SuperadminAdmin(admin.ModelAdmin):
    model = SuperAdminusers
    list_display = ('company_name','admin_user','active_status')

class AdminAdmin(admin.ModelAdmin):
    model = Adminusers
    list_display = ('admin_user','manager','active_status')

class MangerAdmin(admin.ModelAdmin):
    model = Managerusers
    list_display = ('manager','employee','active_status')

admin.site.register(UserPermission, UserPermissionAdmin)
admin.site.register(SuperAdminusers, SuperadminAdmin)
admin.site.register(Adminusers, AdminAdmin)
admin.site.register(Managerusers, MangerAdmin)
