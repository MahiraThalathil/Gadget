from django.contrib import admin
from . models import *
# Register your models here.


class catagAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(catag,catagAdmin)


class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','img','price','stock']
    list_editable=['price','img','stock']
    prepopulated_fields={'slug':('name',)}

admin.site.register(products,prodAdmin)