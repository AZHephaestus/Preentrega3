from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('game/list', views.game_list, name= "game_list"),
    path('game/create', views.game_create, name= "game_create"),
    path('genre/list', views.genre_list, name= "genre_list"),
    path('genre/create', views.genre_create, name= "genre_create"),
    path('gamebygenre/list', views.gamebygenre_list, name= "gamebygenre_list"),
    path('gamebygenre/create', views.gamebygenre_create, name= "gamebygenre_create"),
]
