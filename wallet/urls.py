"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webpage.views import index, profile
from api.views import Contact, Transaction, IsContact
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('profile/<str:address>',profile, name='profile'),
    path('api/contact/', Contact.as_view(), name='api-contact'),
    path('api/tx/', Transaction.as_view(), name='api-transaction'),
    path('api/iscontact/', IsContact.as_view(), name='api-iscontact')
]

urlpatterns = format_suffix_patterns(urlpatterns)


