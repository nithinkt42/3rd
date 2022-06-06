
from django.urls import path
from  . import views

urlpatterns =[
    path('kt3/',views.html3,name='home'),
    path('kt4/',views.html4)
     ]