from django.urls import path
from courses.views import join_course

urlpatterns = [
    path('join-course/', join_course, name='join_course'),


]