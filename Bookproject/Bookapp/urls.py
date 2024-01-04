from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book'),
    path('books/<int:pk>/', views.book_detail, name='book-update'),
        
    
]