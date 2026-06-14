from django.urls import path
from courses.views import join_course, my_courses, my_courses_detail

urlpatterns = [
    path('join-course/', join_course, name='join_course'),
    path('my-courses/', my_courses, name="my_courses"),
    path('my-courses/<str:course_id>/', my_courses_detail, name="my_courses_detail")


]