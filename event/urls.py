"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', views.home, name = 'home'),
    path('owner_page/',views.owner, name = 'owner'),
    path('vendor_page/',views.vendor, name = 'vendor'),
    path('guest_page/',views.guest, name = 'guest'),
    path('owner_page/create_event',views.create_event, name = 'create_event')
]
"""    path('vendor/vendor_event',views.vendor_event, name = 'vendor_event'),
    path('vendor/owner_page/create_event/create_success',views.create_success,name = 'create_success'),
    path('guest_page/guest_event',views.guest_event, name = 'guest_event')
]
"""
