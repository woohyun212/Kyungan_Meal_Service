from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^keyboard/', views.keyboard),
    #url(r'^message$', views.answer),
    path('<message>/', views.answer),
    #path('', views.answer, name='post_list'),
]