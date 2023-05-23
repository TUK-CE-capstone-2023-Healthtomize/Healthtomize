from django.urls import path, include
from rest_framework import routers
from . import views
from .views import foodViewset

router=routers.DefaultRouter()
router.register(r'food',foodViewset)

urlpatterns = [
    path('', views.index, name='index'),
    path('food_info_input', views.food_info_input, name='food_info_input'),
    path('list', views.food_list, name='food_list'),
    path('food_input', views.food_input, name='food_input'),
    path('feedbackw', views.feedback, name='feedback'),
    path('csvinput', views.csvinput, name='csvinput'),
    path('api', include(router.urls)),
    path('nutrient', views.foodcal,name='foodcal'),
    path('feedback', views.feedback_api,name='feedback_api'),

]