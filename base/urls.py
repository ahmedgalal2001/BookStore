from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def unauthenticated_user(view_func, redirect_url='/'):
    """
    Decorator for views that checks that the user is not logged in.
    If the user is logged in, they will be redirected to the specified URL.
    """
    return user_passes_test(lambda user: not user.is_authenticated, login_url=redirect_url)(view_func)

urlpatterns = [
    path('', login_required(views.bookstore,login_url='/user/login/') , name="bookstore"),
    path('bookstore', login_required(views.bookstore, login_url='/user/login/') , name="bookstore"),
    path('bookstore/add', login_required(views.bookstoreAdd,login_url='/user/login/'), name="bookstoreAdd"),
    path('bookstore/show/<str:book_id>/',login_required(views.bookstoreShow,login_url='/user/login/'), name="bookstoreShow"),
    path('bookstore/edit/<str:book_id>/',  login_required(views.bookstoreEdit,login_url='/user/login/'), name="bookstoreEdit"),
    path('bookstore/delete/<str:book_id>/',login_required(views.bookstoreDelete,login_url='/user/login/') , name="bookstoreDelete"),
    path('user/login/', unauthenticated_user(views.userlogin), name="userlogin"),
    path('user/logout/', views.userlogout, name="userlogout"),
    path('user/register/', unauthenticated_user(views.userregister), name="userregister"),
]
