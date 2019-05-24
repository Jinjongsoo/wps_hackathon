"""config URL Configuration

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
from django.urls import path,include
from road import views as road_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('road.urls')),
    path('road/', include('road.urls')),
    path('account/', include('allauth.urls')),
    # path('account/', include('django.contrib.auth.urls')),
    # # 회원가입
    # path('account/signup', road_views.CreateUserView.as_view(), name = 'signup'),
    # # 회원가입 후 로그인
    # path('account/signup_done', road_views.RegisteredView.as_view(),name = 'create_user_done'),
]
