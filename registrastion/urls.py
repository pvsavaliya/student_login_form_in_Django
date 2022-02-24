from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from registrastion import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.data,name='data'),
    
    path('logout/',views.logout,name='logout'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)