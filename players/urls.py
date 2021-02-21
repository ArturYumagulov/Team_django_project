from django.urls import path
from .views import PlayersListView, PlayerDetailViews

urlpatterns = [
    path("list/", PlayersListView.as_view(), name="players_list"),
    path("detail/<int:pk>/", PlayerDetailViews.as_view(), name='detail'),
]