from . import views
from django.urls import path
urlpatterns=[
    path('register',views.register,name='register'),
    path('reregister', views.reregister, name='reregister'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('userhome',views.userhome,name='userhome'),
    path('user',views.user,name='user'),
    path('index', views.index, name='index'),
]