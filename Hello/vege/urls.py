from django.contrib import admin
from django.urls import path
from vege import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path("", views.receipe, name='vege'),
    path("details",views.name, name="details"),
    path("delete_receipe/<id>",views.delete_receipe, name="delete_receipe"),
    path("update_receipe/<id>",views.update_receipe, name="update_receipe"),
    path("login",views.user_login, name="user_login"),
    path("register",views.user_register, name="user_register"),
    path("logout",views.user_logout, name="user_logout")
]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  