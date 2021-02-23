"""bug_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from bug_app.views import login_view, ticket_view, logout_view, submit_view, ticket_details, user_details, ticket_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login_view'),
    path('', ticket_view, name='ticket_page'),
    path('logout/', logout_view, name='logout_view'),
    path('submit/', submit_view, name='submit_view'),
    path('edit/<int:ticket_id>/',ticket_edit, name='ticket_edit'),
    path('ticket/<int:ticket_id>/', ticket_details, name='ticket_details'),
    path('user/<int:user_id>/', user_details, name='user_details'),
]
