from django.contrib import admin
from modelapp.models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['cname','tname','sdate','duration']
admin.site.register(Course,CourseAdmin)
