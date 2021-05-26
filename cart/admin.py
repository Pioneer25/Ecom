from django.contrib import admin
from cart.models import Order,OrderItem
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class OrderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(OrderItem,OrderAdmin)
admin.site.register(Order)
