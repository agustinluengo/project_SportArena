from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='users-index'),
    path('signup/', views.signup, name='signup'),
]