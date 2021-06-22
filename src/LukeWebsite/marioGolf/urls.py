from django.urls import path
import marioGolf.views as views

urlpatterns = [
    path('', views.base_views.Dashboard.as_view(), name='marioGolfHome'),
    path('characters/', views.base_views.CharacterList.as_view(), name='characterListView'),
    path('characters/<int:pk>/', views.base_views.CharacterDetailView.as_view(), name='detailCharacter'),
    path('players/<int:pk>/', views.base_views.PlayerDetailView.as_view(), name='detailPlayer'),
]