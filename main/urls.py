from django.urls import path
from . import views

urlpatterns =[
    path('projects/',views.projects, name='projects'),
    path('languages/',views.languages, name='languages'),
    path('resume/',views.resume, name = 'resume'),
    path('',views.index, name='index')

]