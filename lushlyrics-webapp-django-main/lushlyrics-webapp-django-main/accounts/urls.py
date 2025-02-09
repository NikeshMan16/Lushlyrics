# myproject/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
