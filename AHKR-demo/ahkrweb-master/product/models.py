from django.db import models
# Create your models here.

class Product(models.Model):
    productid = models.CharField(verbose_name='Product id', max_length=256, blank=False, null=True)
    boxcount = models.IntegerField(verbose_name='Box count', blank=False, null=True)
    mfg_date = models.DateField(verbose_name='Manufacturing Date')
    profile_pic = models.ImageField(upload_to='images/product', blank=True, null = True)
    product_status = models.BooleanField(verbose_name='Product Status', default=False)

    def __str__(self):
        return self.productid
