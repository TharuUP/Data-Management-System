"""
URL configuration for tech_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reports.views import redirect_after_login
from django.contrib.auth import views as auth_views
from reports.views import custom_login_redirect
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView



class LogoutViewAllowGet(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Optional
    path('login/', custom_login_redirect, name='custom_login_redirect'),    # This is what we'll use
    path('redirect-after-login/', redirect_after_login, name='redirect_after_login'),
    path('', include('reports.urls')), 
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'), 
  
]
