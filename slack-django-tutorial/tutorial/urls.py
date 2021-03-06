"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from slackbot import views
from django.contrib.auth import views as proj_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/login/', views.SignIn.as_view(), name='login'),
    url(r'^account/logup/', views.SignUp.as_view(), name='register'),
    url(r'^account/logout/$', proj_views.logout, name='logout', kwargs={'next_page': 'TeamsList'}),
    url(r'', include("slackbot.urls")),
]
