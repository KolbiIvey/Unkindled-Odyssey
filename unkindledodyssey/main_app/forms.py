from django.forms import ModelForm
from .models import Character, STARTING_CLASS


class CharacterForm(ModelForm):
    class Meta:
         model = Character
         fields = ['name', 'starting_class', 'level']