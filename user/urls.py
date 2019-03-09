from django.urls import path

from .import views

urlpatterns =[
    path('home/<int:page>.html',views.homeView,name='home'),
    path('login.html',views.loginView,name='login'),
    path('logout.html',views.logoutView,name='logout'),
]