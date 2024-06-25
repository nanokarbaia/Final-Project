from django.contrib import admin
from .models import Pict

from .models import JobCategory, JobListing, Applicant, User


# Register your models here.

admin.site.register(Pict)

admin.site.register(JobCategory)

admin.site.register(JobListing)

admin.site.register(Applicant)

# admin.site.register(User)








# @admin.register(JobCategory)
# class JobCategoryAdmin(admin.ModelAdmin):
#     list_display = ['title']
#
# @admin.register(JobListing)
# class JobListingAdmin(admin.ModelAdmin):
#     list_display = ['title', 'company', 'location']
#     list_filter = ['category', 'location']
#     search_fields = ['title', 'company', 'description']
#
# @admin.register(Applicant)
# class ApplicantAdmin(admin.ModelAdmin):
#     list_display = ['job_listing', 'user']
#     list_filter = ['job_listing', 'user']
#     search_fields = ['user__username', 'job_listing__title']


