"""isolated_shopping URL Configuration

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
from django.urls import path, include
from product import views as p_views
from shopping_basket import views as sb_views
from tokens import views as t_views
from gitwebhook import views as g_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('product/', p_views.ProductProcess.as_view(), name='product_process'),
    path('basket/<int:pk>', sb_views.BasketProcess.as_view(), name='basket_process'),
    path('tokens/speech-to-text', t_views.SpeechToTextTokenProcess.as_view(), name='speech_to_text_process'),
    path('tokens/text-to-speech', t_views.TextToSpeechTokenProcess.as_view(), name='text_to_speech_process'),
    path('git-webhook/', g_views.UpdateServer, name='update_server'),
]
