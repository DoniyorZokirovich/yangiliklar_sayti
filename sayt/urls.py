from django.urls import path
from .views import *
from .auth import regis,login,logout


urlpatterns = [
    path("",index,name='index'),
    path("ser/",ser,name='search'),
    path("con/",con,name='contact'),
    path("cat/<int:_id>/",cat,name='category'),
    path("view/<int:pk>/",view,name='view'),
    path("login/",login,name = 'login'),
    path("regis/",regis,name = 'regis'),
    path("logout/",logout,name = 'logout'),
    path("logout/<int:conf>/",logout,name = 'logout_conf')
]