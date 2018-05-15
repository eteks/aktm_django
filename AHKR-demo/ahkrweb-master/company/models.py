from django.db import models
from product.models import Product


# Create your models here.
class Company(models.Model):
    com_name = models.CharField(verbose_name='Company ', max_length=256, blank=False, null=True)
    company_image = models.ImageField(verbose_name='Company image',upload_to='images/company', blank=True, null = True)
    company_status = models.BooleanField(verbose_name='Company Status', default=False)

    def __str__(self):
        return self.com_name

class AssignProduct(models.Model):
    company = models.ForeignKey(Company, verbose_name='Company', blank = False, null = True, related_name = 'company_name')
    branch = models.CharField(verbose_name='Branch name ', max_length=256, blank=False, null=True)
    product = models.OneToOneField(Product, verbose_name='Product', blank = False, null = True, related_name = 'assign_product')
    place_of_position = models.TextField(verbose_name='Place of position', blank=True, null = True)
    address = models.TextField(verbose_name='Address', blank=True, null = True)

    def __str__(self):
        return self.branch
