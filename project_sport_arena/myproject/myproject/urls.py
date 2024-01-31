from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp import urls as myapp_urls
from users import views as user_views
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls)),
    path('users/signup/', include(users_urls)),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('',include(myapp_urls)),
]
