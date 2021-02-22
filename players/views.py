from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Comments
from .forms import CommentPlayerForms
from django.views.generic import ListView, DetailView, View
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


class AddComment(View):
    def post(self, request, pk):
        form = CommentPlayerForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.player_id = pk
            form.save()
        return redirect('players:detail', pk)


class Search(ListView):
    model = Player
    template_name = 'players/list.html'
    context_object_name = 'players'

    def get_queryset(self):
        u = Player.objects.filter(last_name__icontains=self.request.GET.get("q"))
        if len(u) == 0:
            u = Player.objects.filter(first_name__icontains=self.request.GET.get("q"))
            if len(u) == 0:
                return u.all()
            else:
                return u.all()
        return u.all()

