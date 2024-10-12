from django.contrib import admin
from .models import Phone
# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    # Указывает что показывать в админке
    list_display = 'id', 'name', 'price', 'lte_exists',

    def __str__(self):
        return f'{self.name}'
