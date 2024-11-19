"""
URL configuration for pro1 project.

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
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from app1.views import ContactViewset,EducationdetailViewset,FamilydetailsViewset,PartnerprefarencedetailsViewset

router=SimpleRouter()
router.register('contact',ContactViewset,basename='contact')
router.register('education',EducationdetailViewset,basename='education')
router.register('family',FamilydetailsViewset,basename='family')
router.register('partner',PartnerprefarencedetailsViewset,basename='partner')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include(router.urls))
]
