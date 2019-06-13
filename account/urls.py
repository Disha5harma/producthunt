
from django.urls import path,include
from .import views

urlpatterns = [
path('Signup',views.Signup,name='Signup'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
]