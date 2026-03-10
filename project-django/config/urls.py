from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from users.views import register


urlpatterns = [

    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('', LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', register, name='register'),

]