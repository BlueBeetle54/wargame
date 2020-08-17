"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static

from datetime import datetime
from backend import views as indexView
from rank import views as rankView
if settings.STARTING < datetime.now() < settings.ENDING:
    urlpatterns = [
        path('', indexView.index, name = 'index'),
        path('admin/', admin.site.urls),
        path('notice/', include('notice.urls')),
        path('account/', include('account.urls')),
        path('challenge/', include('prob.urls')),
        path('rank/', rankView.ListRank, name = 'rank'),
        ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path('', indexView.beforeStart, name = 'index'),
        path('admin/', admin.site.urls),
    ]
