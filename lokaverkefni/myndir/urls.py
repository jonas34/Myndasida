from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^photos/', views.photos, name='photos'),
    #url(r'^comments/', views.comments, name='comments'),
]
