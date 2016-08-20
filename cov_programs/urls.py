"""cov_programs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import serializers, viewsets, routers

from cov_search import views

router = routers.DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'sites', views.SiteViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'days', views.DayViewSet)
router.register(r'agegroups', views.AgeGroupViewSet)
router.register(r'instructors', views.InstructorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
