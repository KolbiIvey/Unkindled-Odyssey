from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from .forms import CharacterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import openai
import os


# grabbing api ky from .env and setting api key to variable
API_KEY = os.environ['API_KEY']

#returns the home.html template when the homepage is requested
def home(request):
  return render(request, 'home.html')

#does the same as the home fucntion, except it returns the about.html
def about(request):
  return render(request, 'about.html')

#returns the 'index.html' template and a queryset of Character objects belonging to the current user
@login_required
def characters_index(request):
      #grabbing all charcters that belong to current user
    characters = Character.objects.filter(user=request.user)
    #renders the index page with the characters queryset
    return render(request, 'characters/index.html', {'characters': characters})

#returns the 'detail.html' template with the requested Character and its associated Story
@login_required
def characters_detail(request, character_id):
  #grabbing a specific character
  character = Character.objects.get(id=character_id)
  #renders the charcters detail page with associated story
  return render(request, 'characters/detail.html', {
    'character': character,
    'story': character.story,
  })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#view for creating a new character
class CharacterCreate(LoginRequiredMixin, CreateView):
  model = Character
  form_class = CharacterForm
  template_name = 'main_app/characters_create.html'
  # This method is called when the user submits the form on the create page.
  # It sets the current user as the owner of the new character and saves the form.
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#updates the specified character using the same form as CreateCharacter
#Then redirects the user back to the character index page
class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_update_form.html'
    success_url = '/characters'

#deletes specified character then redirects user back ti charcter index page
class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters'


@login_required
def character_story(request, character_id):
    #grabbing a specific character object with id
    character = Character.objects.get(id=character_id)

    #setting Open Ai api key
    openai.api_key = API_KEY
    
    #setting the prompt that openai will use for generateing story about the character
    prompt = f"Generate a short story about {character.name} in the story of of the video game Dark Souls 3, where {character.name} is a {character.get_starting_class_display()} brandishing a {character.get_starting_weapon_display()}, please make the story 2 paragraphs long."
    #using open ai api to generate short story based on the prompt
    response = openai.Completion.create(
       engine="text-davinci-002",
       prompt=prompt,
       max_tokens=3000,
       n=1,
       stop=None,
       temperature=0.9,
    )
    #grabbing the story that the api has generated
    story = response.choices[0].text.strip()
    #updating the story field of the character with the generated story
    character.story = story
    #saving the updated character to the database
    character.save()

     # Rendering the detail.html template with the character object and generated story
    return render(request, 'characters/detail.html', {
       'character': character,
       'story': story
    })


