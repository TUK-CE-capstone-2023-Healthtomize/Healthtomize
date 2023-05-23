from django.urls import path, include

from . import views
from rest_framework import routers
from .views import userViewset


router=routers.DefaultRouter()
router.register(r'user',userViewset)
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.member_reg, name='member_reg'),
    path('login', views.member_login, name='member_login'),
    path('logout', views.member_logout, name='member_logout'),
    path('list', views.user_list, name='user_list'),
    path('api',include(router.urls)),
    path('userfind',views.userfind,name='userfind')
]
