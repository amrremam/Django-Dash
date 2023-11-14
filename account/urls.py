from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('docs/', views.doctor_list, name='doctor_list'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.my_profile, name='profile'),
    path('update/', views.update_profile, name='update'),
    path('<slug:slug>/', views.doctor_detail, name='doctor_detail'),
]
