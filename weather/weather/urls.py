"""
URL configuration for weather project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from sun.views import suns, suns_date, health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
    path("sun/", suns),
    # re_path(r"suns/(?P<country>[A-Z]{1}[a-z]+)$", suns),
    # path("suns/<str:country>", suns),
    # path("suns/<str:date>", suns_date), # Impossible car match avec `suns/<str:country>`
    re_path(r"suns/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})$", suns_date),
]
