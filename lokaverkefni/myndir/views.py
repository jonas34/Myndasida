from django.shortcuts import render
from .models import MyUser
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    username = request.GET['username']
    dateofbirth = request.GET['dateofbirth']
    password = request.GET['password']
    u = MyUser.objects.create_user(email, dateofbirth, password)
    u.save()
    return HttpResponse("you are in register")
