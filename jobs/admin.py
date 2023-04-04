# Register your models here.

from django.contrib import admin
from .models import Job
from .models import JobApplication
from .models import EmailSubscription

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'job_category', 'company', 'date_posted')
    list_filter = ('job_type', 'job_category', 'company')
    search_fields = ('title', 'description', 'location', 'requirements')


admin.site.register(JobApplication)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    list_filter = ('submitted_at',)  # Use string value here
    search_fields = ('name', 'email', 'phone')

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')

