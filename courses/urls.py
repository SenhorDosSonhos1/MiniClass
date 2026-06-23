from django.urls import path
from courses.views import join_course, my_courses, my_courses_detail, lesson_detail, exercise_detail

urlpatterns = [
    path('join-course/', join_course, name='join_course'),
    path('my-courses/', my_courses, name="my_courses"),
    path('my-courses/<str:course_id>/', my_courses_detail, name="my_courses_detail"),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('exercise/<int:exercise_id>/', exercise_detail, name="exercise_detail")
]