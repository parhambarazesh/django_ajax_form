from django.urls import path
from . import views

#from config import dash_apps

urlpatterns=[
   path('',views.index),
   path('call_backend/', views.call_backend,name='call_backend'),
]
