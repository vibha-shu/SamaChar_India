from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('login/',views.login),
    path('videos/',views.video),
    path('viewnews/',views.viewnews),
    path('viewmore/',views.viewmore),
    path('vnews/',views.vnews),
]