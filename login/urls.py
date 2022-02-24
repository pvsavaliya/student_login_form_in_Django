from django.contrib import admin
from django.urls import path,include

from login import views


urlpatterns = [
    path('',views.index,name='index'),
    path('data/',views.studata,name='studata'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]
