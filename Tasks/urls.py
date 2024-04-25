"""
URL configuration for Tasks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from . import views
from .views import toggle_complete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('calendar/', views.load_calendar, name="calendar"),
    path('add_task', views.new_task, name="new_task"),
    path('toggle-complete-task/', views.toggle_complete_task, name="toggle_complete_task"),
    path('edit-task/', views.edit_task, name="edit_task"),
    path('delete-task/', views.delete_task, name="delete_task")
]
