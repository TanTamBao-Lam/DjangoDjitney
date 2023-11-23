"""
URL configuration for djangodjitney project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from routes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('lines/', views.LinesView.as_view(), name='lines'),
    path('lines/new', views.CreateLineView.as_view(), name="create_line"),
    path('lines/<pk>/update/', views.UpdateLineView.as_view(), name="update_line"),
    path('lines/<pk>/delete', views.DeleteLineView.as_view(), name="delete_line"),
]
