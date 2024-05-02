from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookstore , name="bookstore"),
    path('bookstore', views.bookstore , name="bookstore"),
    path('bookstore/add', views.bookstoreAdd, name="bookstoreAdd"),
    path('bookstore/show/<str:book_id>/', views.bookstoreShow, name="bookstoreShow"),
    path('bookstore/edit/<str:book_id>/', views.bookstoreEdit, name="bookstoreEdit"),
    path('bookstore/delete/<str:book_id>/', views.bookstoreDelete, name="bookstoreDelete"),
]