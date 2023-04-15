from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/food_info_input', views.food_info_input, name='food_info_input'),
    path('/list', views.food_list, name='food_list'),
    path('/food_input', views.food_input, name='food_input'),

]