from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/',views.log_in,name='login'),
    url(r'^photos/', views.photos, name='photos'),
    #url(r'^comments/', views.comments, name='comments'),
]
