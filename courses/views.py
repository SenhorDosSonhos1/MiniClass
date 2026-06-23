from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from courses.models import Course, Enrollment, Lesson, Exercise, Submission
from django.contrib import messages

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
                print("MATRICULA CRIADA")

                return redirect("my_courses")
            
            messages.error(request, "Você já está matriculado neste curso.")
            return redirect("join_course")
        
        except Course.DoesNotExist:
            messages.error(request, "O código está inválido ou o curso não existe.")
            return redirect("join_course")    
        
    return redirect('join_course')

#Listar todos os cursos que o aluno fez matricula
@login_required(login_url="user_login")
def my_courses(request):
    if request.method == "GET": 
        enrollment = Enrollment.objects.filter(student = request.user)

        return render(request, "courses/my_courses.html", 
                        context = {
                            "courses": enrollment
        })
        
    return redirect("user_login")
# Detalhar o curso do aluno matriculado 
# E listar as lições do curso
@login_required(login_url="user_login") 
def my_courses_detail(request, course_id):
    enrollment = Enrollment.objects.filter(student = course_id)
    try:
    # Verificar se o usuario logado for == ao usuario matriculado
        if Enrollment.objects.get(
                student = request.user,
                course = course_id
            ):
        
            lesson = Lesson.objects.filter(course = course_id)

            return render(request, 'courses/my_course_detail.html', context={
                "courses": enrollment,
                "lessons": lesson
            })
        
    except Enrollment.DoesNotExist:
        print("Erro ao acessar o curso detail")
        return redirect("/gg/")
    
@login_required(login_url="user_login")
def lesson_detail(request, lesson_id):
    if request.method == "GET":
        try:
            if Enrollment.objects.get(
                student = request.user
            ):
                
                lessons = Lesson.objects.filter(id = lesson_id)
                exercises = Exercise.objects.filter(lesson = lesson_id)
                return render(request, 'courses/lesson_detail.html', context = {
                    "lessons": lessons,
                    "exercises": exercises,
                })
            
        except Enrollment.DoesNotExist:
            print("Erro ao acessar o curso detail")
            return redirect("/gg/")
    
def exercise_detail(request, exercise_id):
    if request.method == "GET":
        exercise = Exercise.objects.filter(id = exercise_id)

        return render(request, "courses/exercise_detail.html", context={
        "exercises": exercise
        })
    
    content = request.POST.get("content")

    if content == "":
        print("Probido campos vazios")
    
    if not Submission.objects.filter(exercise = exercise_id, student = request.user).exists():
        try:
            exercise = Exercise.objects.get(id = exercise_id)
            submission = Submission.objects.create(exercise = exercise,
                                                    student = request.user,
                                                    content = content
                                                    )
            
            return HttpResponse("Resposta enviada com sucesso!")
        except Submission.DoesNotExist:
            return HttpResponse("Erro ao enviar a resposta")

    return HttpResponse("Voce já enviou uma resposta!")