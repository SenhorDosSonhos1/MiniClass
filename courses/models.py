from django.db import models
from django.conf import settings
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