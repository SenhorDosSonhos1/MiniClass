from django.urls import path
from accounts.views import user_login, user_register


urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name= 'user_register')
]