from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path("", views.index, name='home'),
    path("receipes/<id>",views.index2, name="receipe"),
    
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  