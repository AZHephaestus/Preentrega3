from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "GWP/index.html")

def game_list(request):
    consult = models.game.objects.all()
    context = {"games": consult}
    return render(request, "GWP/game_list.html", context)

def game_create(request):
    if request.method == "POST":
        form = forms.gameform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_list")
    else:
        form = forms.gameform()
    return render(request, "GWP/game_creation.html", {"form": form})        

def genre_list(request):
    consult = models.gamegenre.objects.all()
    context = {"genres": consult}
    return render(request, "GWP/genre_list.html", context)

def genre_create(request):
    if request.method == "POST":
        form = forms.genreform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("genre_list")
    else:
        form = forms.genreform()
    return render(request, "GWP/genre_creation.html", {"form": form})    

def gamebygenre_list(request):
    consult = models.gamebygenre.objects.all()
    context = {"gamesgenre": consult}
    return render(request, "GWP/gamebygenre_list.html", context)

def gamebygenre_create(request):
    if request.method == "POST":
        form = forms.gamebygenreform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gamebygenre_list")
    else:
        form = forms.gamebygenreform()
        context = {"form": form}
    return render(request, "GWP/gamebygenre_creation.html", context) 