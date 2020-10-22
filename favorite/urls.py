from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import favorite, favorite_list, NotFavorite

app_name = 'favorite'

urlpatterns = [
    path('', favorite, name='favorite'),
    path('favorite_list/',favorite_list,name='favorite_list'),
    path('not_favorite/',NotFavorite.as_view(),name='not_favorite'),
]