from django.contrib import admin
from .models import Product
from company.models import AssignProduct
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('productid', 'boxcount', 'mfg_date', 'product_status','get_assigned_company')

    def get_assigned_company(self, obj):
        ap = AssignProduct.objects.select_related().filter(product__pk = obj.id)
        if ap.count():
            return ap.values('company__com_name')[0]['company__com_name']
        else:
            return 'Not assigned'

    get_assigned_company.short_description = 'Assigned Company'
