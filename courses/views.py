from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Profile
from courses.models import Course, Enrollment, Lesson

# Create your views here.
def join_course(request):
    if request.method == "GET":
        return render(request, 'courses/join_course.html')
    
    if request.user.profile.role == "A":
        try:
            token = request.POST.get('token')
            course = Course.objects.get(acess_token = token) # Ex '12345'

            if not Enrollment.objects.filter(student=request.user, course=course).exists():
                Enrollment.objects.create(student=request.user, course=course)

                return HttpResponse('Voce foi matriculado no curso')
            return HttpResponse('Você ja esta matriculado neste curso')
        except Course.DoesNotExist:
            return HttpResponse('Código errado ou curso não existente')    
        
    return redirect('join_course')

def my_courses(request):
    if request.method == "GET":
        courses = Enrollment.objects.filter(student = request.user)
        return render(request, "courses/my_courses.html", 
                      context = {
                          "courses": courses
        })
    
def my_courses_detail(request, course_id):
    courses = Enrollment.objects.filter(course = course_id)
    lesson = Lesson.objects.filter(course = course_id)
    return render(request, 'courses/my_course_detail.html', context={
        "courses": courses,
        "lessons": lesson
    })
