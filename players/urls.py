from django.urls import path
from .views import PlayersListView, PlayerDetailViews, AddComment, Search

urlpatterns = [
    path("list/", PlayersListView.as_view(), name="players_list"),
    path("detail/<int:pk>/", PlayerDetailViews.as_view(), name='detail'),
    path("comment/<int:pk>/", AddComment.as_view(), name='add_comment'),
    path("search/", Search.as_view(), name='search')

]