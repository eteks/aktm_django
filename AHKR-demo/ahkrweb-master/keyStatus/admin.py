from django.contrib import admin
from django.db import models
from product.models import Product
from company.models import Company,AssignProduct
from django.contrib.auth.models import User
from .models import KeyStatus
from users.models import Users
from django.contrib.auth.models import Permission


# Creating manual key status model
# The admin can enter the status of the key manually.
class KeyStatusAdmin(admin.ModelAdmin):
	model = KeyStatus, Users
	list_display= ('company','branch','product_id','box_id','key_status','createdby','createdat')

	def get_queryset(self, request):
		qs = super(KeyStatusAdmin, self).get_queryset(request)
		user_name = request.user
		if(request.user.is_superuser):
			return qs
		else:
			return qs.filter(createdby = user_name)
	
admin.site.register(KeyStatus, KeyStatusAdmin)
