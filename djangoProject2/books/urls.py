from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from . import views
from .views import *


router = routers.DefaultRouter()

urlpatterns = [
    path('', upload_book, name='upload_book'),
    path('upload/', upload_book, name='upload_book'),

    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('list/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    # path('admin/', admin.site.urls),
]
