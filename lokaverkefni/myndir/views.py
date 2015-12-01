from django.shortcuts import render, redirect
from .models import MyUser, Photos, Comments
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
    response = HttpResponse(photos)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def comments(request):
    comments = Comments.objects.all()
    comments = serializers.serialize("json", comments)
    response = HttpResponse(comments)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def postcomment(request):
    comment = request.GET['comment']
    photoId = request.GET['id']
    photos = Photos.objects.get(pk=photoId)
    user = MyUser.objects.get(pk=photos.author.id)
    c = Comments.objects.create(text=comment, photo=photos, author=user)
    return HttpResponse("comment posted")
