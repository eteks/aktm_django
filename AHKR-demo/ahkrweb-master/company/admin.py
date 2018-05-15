from django.contrib import admin
from .models import Company,AssignProduct
from product.models import Product
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('com_name', 'company_image', 'company_status')


class AssignProductAdmin(admin.ModelAdmin):
    list_display = ('get_company', 'branch', 'get_product','place_of_position','address')

    def get_company(self, obj):
        return obj.company.com_name
    get_company.short_description = 'Company Name'

    def get_product(self, obj):
        return obj.product.productid
    get_product.short_description = 'Product ID'


admin.site.register(Company, CompanyAdmin)
admin.site.register(AssignProduct, AssignProductAdmin)
