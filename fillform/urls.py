from django.urls import path
from .import views

urlpatterns= [
 path('fill/', views.userdata, name='userdata'),
    path('success/', views.thankyou, name='thankyou'),
    path('', views.userdata, name='home'),
   
    
]

