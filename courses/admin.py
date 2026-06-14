from django.contrib import admin

# Register your models here.
from courses.models import Course, Enrollment, Lesson,Exercise, Submission

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(Submission)