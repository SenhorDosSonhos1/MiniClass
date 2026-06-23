from django.db import models
from django.conf import settings

from django.db.models.constraints import UniqueConstraint
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT) #SET_NULL
    description = models.TextField()
    acess_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Curso: {self.name} - Professor: {self.teacher}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
           UniqueConstraint(
               fields=['student', 'course'], name="unique_enrollment"
            )
        ]


    def __str__(self):
        return f"Aluno: {self.student} - Curso: {self.course}"

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lição: {self.title} - Curso: {self.course}"
    
class Exercise(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exercicio: {self.title} - Tema: {self.lesson}"
    
class Submission(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["exercise", "student"], name="unique_submission"
            )
        ]
    
    def __str__(self):
        return f"Exercicio: {self.exercise} - Aluno: {self.student}"