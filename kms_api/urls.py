from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    #path('keyboard/', views.keyboard),
    path('answer/', views.answer)

]
