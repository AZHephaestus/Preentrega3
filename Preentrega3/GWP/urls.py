from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', index, name="index"),
    #path('game/list', views.game_list, name= "game_list"),
    path('game/list', GameList.as_view(), name= "game_list"),
    #path('game/create', views.game_create, name= "game_create"),
    path('game/form', GameCreate.as_view(), name= "game_form"),
    #path('genre/list', views.genre_list, name= "genre_list"),
    path('genre/list', GenreList.as_view(), name= "genre_list"),
    #path('genre/create', views.genre_create, name= "genre_create"),
    path('genre/form', GenreCreate.as_view(), name= "genre_form"),
    #path('gamebygenre/list', views.gamebygenre_list, name= "gamebygenre_list"),
    path('gamebygenre/list', GameByGenreList.as_view(), name= "gamebygenre_list"),
    #path('gamebygenre/create', views.gamebygenre_create, name= "gamebygenre_create"),
    path('gamebygenre/form', GameByGenreCreate.as_view(), name= "gamebygenre_form"),
    path('add/index', add_index, name= "add_index"),
    #path('game/update/<id=pk>/', views.game_update, name= "game_update"),
    path('game/update/<int:pk>', gameUpdate.as_view(), name= "game_update"),
    #path('game/delete/<id=pk>/', views.game_delete, name= "game_delete"),
    path('game/delete/<int:pk>', GameDelete.as_view(), name= "game_delete"),
    path('game/detail/<int:pk>', GameDetail.as_view(), name= "game_detail"),
    path('login/', CustomLoginView.as_view(), name= "login"),
    path('logout/', LogoutView.as_view(template_name="GWP/logout.html"), name= "logout"),
    path('register/', register, name= "register"),
    path('about/', about, name= "about"),
]
