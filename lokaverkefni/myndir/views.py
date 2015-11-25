from django.shortcuts import render
from .models import MyUser, Photos
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


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

def photos(request):
    photos = Photos.objects.all()
    photos = serializers.serialize("json", photos)
    photos_json = json.dumps(list(photos), cls=DjangoJSONEncoder)
    return HttpResponse(photos)
