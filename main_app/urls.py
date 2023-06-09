from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.characters_index, name='index'),
    path('characters/<int:character_id>/', views.characters_detail, name='detail'),
    path('characters/<int:character_id>/story/', views.character_story, name='character_story'),
    path('accounts/signup/', views.signup, name='signup'),
    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
]

