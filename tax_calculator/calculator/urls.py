from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calc', views.calc, name='calc'),
    path('News', views.news, name='news'),
    path('news_sentence', views.news, name='news_sentence')
]
