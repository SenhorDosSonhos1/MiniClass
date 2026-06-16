from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    return HttpResponse("O usuario nao esta logado")