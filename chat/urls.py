"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.zeige, name='Zeige'),
    url(r'^home/$', views.zeige, name='Zeige'),
    url(r'^add/', views.add, name='Zeige'),
    url(r'^edit/$', views.get_name, name='Zeige'),
    url(r'^addgd', views.addgd, name='Zeige'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/home'}, name='logout'),
]
