"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from tasks.views import GenericCompleteTaskView, GenericPendingTaskView, GenericTaskCreateView, GenericTaskDeleteView, GenericTaskDetailView, GenericTaskUpdateView, GenericTaskView, UserCreateView, UserLoginView, home_view

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("user/signup", UserCreateView.as_view(), name="create_user"),
    path("user/login", UserLoginView.as_view(), name="login_user"),
    path("tasks", GenericTaskView.as_view(), name="tasks"),
    path("user/logout", LogoutView.as_view(), name="logout_user"),
    path("create-task", GenericTaskCreateView.as_view(), name="create_task"),
    path("update-task/<pk>", GenericTaskUpdateView.as_view(), name="update_task"),
    path("detail-task/<pk>", GenericTaskDetailView.as_view(), name="detail_task"),
    path("delete-task/<pk>", GenericTaskDeleteView.as_view(), name="delete_task"),
    path("completed-tasks", GenericCompleteTaskView.as_view(), name="completed_tasks"),
    path("pending-tasks", GenericPendingTaskView.as_view(), name="pending_tasks"),
]
