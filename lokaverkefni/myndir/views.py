from django.shortcuts import render, redirect
from .models import MyUser, Photos
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.conf import settings


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

def log_in(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user_name=request.GET['Username']
    passw = request.GET['Password']
    user = authenticate(email=user_name, password=passw)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("login successful")
        else: return HttpResponse("disabled account")
    else: return HttpResponse("invalid login")

def photos(request):
    photos = Photos.objects.all()
    photos = serializers.serialize("json", photos)
    photos_json = json.dumps(list(photos), cls=DjangoJSONEncoder)
    return HttpResponse(photos)
