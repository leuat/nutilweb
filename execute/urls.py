from django.conf.urls import url
from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
   	path('run/', views.run, name='run'),
]