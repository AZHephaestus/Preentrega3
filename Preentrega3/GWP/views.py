from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def index(request):
    return render(request, "GWP/index.html")

def about(request):
    return render(request, "GWP/about.html")

#def game_list(request):
#    consult = models.game.objects.all()
#    context = {"games": consult}
#    return render(request, "GWP/game_list.html", context)
class GameList(ListView):
    model = game

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = game.objects.filter(nombre__icontains=consulta)
        else:
            object_list = game.objects.all()
        return object_list

#def game_create(request):
#    if request.method == "POST":
#        form = forms.gameform(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("game_list")
#    else:
#        form = forms.gameform()
#    return render(request, "GWP/game_creation.html", {"form": form})

class GameCreate(LoginRequiredMixin, CreateView):
    model = game
    form_class = gameform
    success_url = reverse_lazy("game_list") 
    
#def genre_list(request):
#    consult = models.gamegenre.objects.all()
#    context = {"genres": consult}
#    return render(request, "GWP/genre_list.html", context)

class GenreList(ListView):
    model = gamegenre

#def genre_create(request):
#    if request.method == "POST":
#        form = forms.genreform(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("genre_list")
#    else:
#        form = forms.genreform()
#    return render(request, "GWP/genre_creation.html", {"form": form})    
    
class GenreCreate(LoginRequiredMixin, CreateView):
    model = gamegenre
    form_class = genreform
    success_url = reverse_lazy("genre_list") 

#def gamebygenre_list(request):
#    consult = models.gamebygenre.objects.all()
#    context = {"gamesgenre": consult}
#    return render(request, "GWP/gamebygenre_list.html", context)
    
class GameByGenreList(ListView):
    model = gamebygenre

#def gamebygenre_create(request):
#    if request.method == "POST":
#        form = forms.gamebygenreform(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("gamebygenre_list")
#    else:
#        form = forms.gamebygenreform()
#        context = {"form": form}
#    return render(request, "GWP/gamebygenre_creation.html", context) 
    
class GameByGenreCreate(LoginRequiredMixin, CreateView):
    model = gamebygenre
    form_class = gamebygenreform
    success_url = reverse_lazy("gamebygenre_list")

@login_required
def add_index(request):
    return render(request, "GWP/add_index.html")

#def game_update(request, pk: int):
#    consulta = game.objects.get(id = pk)
#    if request.method == "POST":
#        form = gameform(request.POST, instance=consulta)
#        if form.is_valid():
#            form.save()
#            return redirect("game_list")
#    else:
#        form = gameform(instance=consulta)
#    return render(request, "GWP/game_form.html", {"form": form})

class gameUpdate(LoginRequiredMixin, UpdateView):
    model = game
    form_class = gameform
    success_url = reverse_lazy("game_list") 

#def game_delete(request, pk: int):
#    consulta = game.objects.get(id = pk)
#    if request.method == "POST":
#        consulta.delete()
#        return redirect("game_list")
#    return render(request, "GWP/game_confirm_delete.html", {"object": consulta})

class GameDelete(LoginRequiredMixin, DeleteView):
    model = game
    success_url = reverse_lazy("game_list")

class GameDetail(DetailView):
    model = game

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "GWP/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "GWP/register.html", {"form": form})

class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = gamegenre
    form_class = genreform
    success_url = reverse_lazy("genre_list") 

class GenreDelete(LoginRequiredMixin, DeleteView):
    model = gamegenre
    success_url = reverse_lazy("genre_list")

class GameByGenreUpdate(LoginRequiredMixin, UpdateView):
    model = gamebygenre
    form_class = gamebygenreform
    success_url = reverse_lazy("gamebygenre_list") 

class GameByGenreDelete(LoginRequiredMixin, DeleteView):
    model = gamebygenre
    success_url = reverse_lazy("gamebygenre_list")

#class GamePurchase(ListView):
#    model = GamePurchaseForm

#class GamePurchaseList(LoginRequiredMixin, ListView):
#    model = game
#
#    def get_queryset(self):
#        if self.request.GET.get("consulta"):
#            consulta = self.request.GET.get("consulta")
#            object_list = game.objects.filter(nombre__icontains=consulta)
#        else:
#            object_list = game.objects.all()
#        return object_list
#
#class GamePurchase(LoginRequiredMixin, DeleteView):
#    model = game
#    success_url = reverse_lazy("gamepurchase_list")

#def game_purchase(request, pk: int):
#    consulta = GamePurchase.objects.get(id = pk)
#    if consulta == pk:
#        consult = models.GamePurchase.objects.all()
#        context = {"gameP": consult}
#        return render(request, "GWP/game_purchase.html", context)

#@login_required
#def game_purchase(request):
#    return render(request, "GWP/game_purchase.html")

#class GamePurchase(ListView):
#    model = GamePurchase