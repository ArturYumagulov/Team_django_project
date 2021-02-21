from django.shortcuts import render
from .models import Player
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PlayersListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = "players/list.html"


class PlayerDetailViews(DetailView):
    queryset = Player.objects.all()
    context_object_name = 'player'
    template_name = "players/detail.html"

