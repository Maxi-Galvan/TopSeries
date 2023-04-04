"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from AppCoder.views import mostrar_mi_template, mostrar_mis_tareas
from SocialTravel.views import index
from TopSeries.views import mostrar_texto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_template/<nombre>/<apellido>', mostrar_mi_template),
    path('mis_tareas', mostrar_mis_tareas, name='mis-tareas'),
    #path('', index)
    path('', mostrar_texto),

]
