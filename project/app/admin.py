from django.contrib import admin
from app.models import vaibhav

# Register your models here.
class vk(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'price',
        'stock',
        'desc'

    ]

admin.site.register(vaibhav,vk)
