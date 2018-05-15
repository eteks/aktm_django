from django.db import models
from product.models import Product
from company.models import Company,AssignProduct
from django.contrib.auth.models import User

# Creating manual key status model
# The user can enter the status of the key manually.
class KeyStatus(models.Model):
	IN = 'IN'
	OUT = 'OUT'
	KEY_STATUS = ((IN,'IN'),(OUT,'OUT'))
	company = models.CharField(verbose_name='Company' , max_length=255 , blank=False ,null=True)
	branch = models.CharField(verbose_name='Branch name' , blank=False , max_length=255, null=True)
	product_id = models.CharField(verbose_name='Product ID', max_length = 255, blank=False, null=True)
	box_id = models.IntegerField(verbose_name='Box ID', blank=False, null=True)
	key_status = models.CharField(verbose_name="Key Status",max_length=255,choices=KEY_STATUS,default=IN)
	createdby = models.CharField(verbose_name='Created By' , max_length=255 , blank=False ,null=True)
	createdat = models.CharField(verbose_name='Created At' , max_length=255 , blank=False ,null=True)

	


	