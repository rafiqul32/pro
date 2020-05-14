from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'occupation')


admin.site.register(Course, CourseAdmin)