"""djangoProject2 URL Configuration

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
from rest_framework import routers
from django.urls import include, path
from . import views
from books import views as bookviews

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', views.api, name='api'),
    # path('', include(router.urls)),
    path('books/',include('books.urls')),
    path('', views.index, name='index'),
    # path('books/upload/', bookviews.upload_book, name='upload_book'),
    # path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)