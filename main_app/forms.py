from django.forms import ModelForm
from .models import Character


class CharacterForm(ModelForm):
    # Defines a ModelForm based on the Character model.
    class Meta:
         # Sets the meta options for the form.
         model = Character  # Uses the Character model as the basis for the form.
         fields = ['name', 'starting_class', 'starting_weapon', 'starting_gift', 'level']
         # Specifies the fields to include in the form, which are name, starting_class,
         # starting_weapon, starting_gift, and level.