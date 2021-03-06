"""zappa_workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.ENVIRONMENT == 'books':
    urlpatterns.append(path('', include('applications.books.urls')))
elif settings.ENVIRONMENT == 'compute_engine':
    urlpatterns.append(path('', include('applications.compute_engine.urls')))
elif settings.ENVIRONMENT == 'front':
    urlpatterns.append(path('', include('applications.front.urls')))
else:
    urlpatterns.extend([
        path('', include('applications.books.urls')),
        path('', include('applications.compute_engine.urls')),
        path('', include('applications.front.urls')),
    ])

