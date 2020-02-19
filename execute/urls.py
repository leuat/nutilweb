from django.conf.urls import url
from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
   	path('run/', views.run, name='run'),
   	path('results/', views.results, name='results'),
 	path('<str:filename>/download/', views.download, name='download'),
]