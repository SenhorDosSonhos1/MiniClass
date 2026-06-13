from django.contrib import admin

# Register your models here.
from courses.models import Course, Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)