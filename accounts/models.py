from django.db import models
from django.contrib.auth.models import User
# Register your models here.

ROLE_CHOICES = [
    ('P', 'Professor'),
    ('A', 'Aluno')
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES,
        default='A'
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"