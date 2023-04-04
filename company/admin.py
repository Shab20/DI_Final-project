from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'location', 'contact_email', 'contact_phone')
    list_filter = ('industry',)
    search_fields = ('name', 'description', 'location', 'industry')
