"""DjangoOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('', include('apps.base_html.urls', namespace='base_html')),
    path('auth/', include('apps.auth_user.urls', namespace='auth_user')),
    path('bill/', include('apps.bill_tracker.urls', namespace='bill_tracker')),
    path('pm/', include('apps.project_manager.urls', namespace='project_manager')),
    path('admin/', admin.site.urls),
]
