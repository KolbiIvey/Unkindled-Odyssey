from django.forms import ModelForm
from .models import Character


class CharacterForm(ModelForm):
    class Meta:
         model = Character
         fields = ['name', 'starting_class', 'starting_weapon', 'starting_gift', 'level']