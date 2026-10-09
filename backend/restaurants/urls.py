from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('restaurant/',views.restaurant_list, name = 'restaurant_list'),
    path('login/',views.login, name = 'login'),
    path('restaurant-detail/',views.restaurant_detail, name = 'restaurant_detail'),
    path('signup/',views.signup, name = 'signup'),
    path('writereview/',views.writereview, name = 'writereview'),
    path('userprofile/',views.userprofile, name = 'userprofile'),
]