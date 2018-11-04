"""imgae_cl_api URL Configuration

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
from django.urls import path
from tf_model_call import views as tf_model_call_view

urlpatterns = [
    path('index/', tf_model_call_view.index),
    path('call_model/', tf_model_call_view.call_model),
    path('upload/', tf_model_call_view.upload),
    path('admin/', admin.site.urls),
]
