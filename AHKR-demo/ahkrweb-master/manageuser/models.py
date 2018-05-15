from django.db import models
from ahkrweb.constant import USER_TYPE
from company.models import Company
from users.models import Users
# Create your models here.
class UserPermission(models.Model):
    user_type = models.CharField(verbose_name = "User type", unique=True, max_length = 50, choices = USER_TYPE, blank = False, null = False)
    can_add_admin = models.BooleanField(verbose_name='Can add admin', default=False)
    can_edit_admin = models.BooleanField(verbose_name='Can edit admin', default=False)
    can_delete_admin = models.BooleanField(verbose_name='Can delete admin', default=False)
    can_viewlog_admin = models.BooleanField(verbose_name='Can view log information admin', default=False)
    can_add_manager = models.BooleanField(verbose_name='Can add manager', default=False)
    can_edit_manager = models.BooleanField(verbose_name='Can edit manager', default=False)
    can_delete_manager = models.BooleanField(verbose_name='Can delete manager', default=False)
    can_viewlog_manager = models.BooleanField(verbose_name='Can view log information manager', default=False)
    can_add_employee = models.BooleanField(verbose_name='Can add employee', default=False)
    can_edit_employee = models.BooleanField(verbose_name='Can edit employee', default=False)
    can_delete_employee = models.BooleanField(verbose_name='Can delete employee', default=False)
    can_viewlog_employee = models.BooleanField(verbose_name='Can view log information employee', default=False)


class SuperAdminusers(models.Model):
    company_name = models.ForeignKey(Company, verbose_name='Company', blank = False, null = True, related_name = 'company')
    admin_user = models.ForeignKey(Users,verbose_name='Admin user', blank = False, null = True,limit_choices_to={'user_type': 'Admin'})
    active_status = models.BooleanField(verbose_name='Active', default=False)

    class Meta:
        unique_together = ('company_name', 'admin_user',)
        verbose_name_plural = "SuperAdmin"

class Adminusers(models.Model):
    admin_user = models.ForeignKey(Users,verbose_name='Admin user', blank = False, null = True,related_name="admin_user", limit_choices_to={'user_type': 'Admin'})
    manager = models.ForeignKey(Users,verbose_name='Manager', blank = False, null = True,limit_choices_to={'user_type': 'Manager'})
    active_status = models.BooleanField(verbose_name='Active', default=False)

    class Meta:
        unique_together = ('admin_user', 'manager')
        verbose_name_plural = "Admin"

class Managerusers(models.Model):
    manager = models.ForeignKey(Users,verbose_name='Manager', blank = False, null = True,limit_choices_to={'user_type': 'Manager'})
    employee = models.ForeignKey(Users,verbose_name='Employee', blank = False, null = True, related_name="employee_user",limit_choices_to={'user_type': 'Employee'})
    active_status = models.BooleanField(verbose_name='Active', default=False)

    class Meta:
        unique_together = ('manager', 'employee')
        verbose_name_plural = "Manager"
