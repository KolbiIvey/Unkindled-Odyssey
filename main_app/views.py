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



API_KEY = os.environ['API_KEY']


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


@login_required
def characters_index(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'characters/index.html', {'characters': characters})

@login_required
def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  # image_url = None
  # if character.starting_class == 'K':
  #    image_url = "../../static/knight.jpeg"
  # # elif character.starting_class == '':
  # #    image_url = ../../
  return render(request, 'characters/detail.html', {
    'character': character,
    'story': character.story,
    # 'image_url': image_url
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


class CharacterCreate(LoginRequiredMixin, CreateView):
  model = Character
  form_class = CharacterForm
  template_name = 'main_app/characters_create.html'

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_update_form.html'
    success_url = '/characters'


class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters'


@login_required
def character_story(request, character_id):
    character = Character.objects.get(id=character_id)

  
    openai.api_key = API_KEY
    
    prompt = f"Generate a short story about {character.name} in the story of of the video game Dark Souls 3, where {character.name} is a {character.get_starting_class_display()} brandishing a {character.get_starting_weapon_display()}, please make the story 2 paragraphs long, and sometimes kill the character."
    response = openai.Completion.create(
       engine="text-davinci-002",
       prompt=prompt,
       max_tokens=3000,
       n=1,
       stop=None,
       temperature=0.9,
    )

    story = response.choices[0].text.strip()
    character.story = story
    character.save()

    return render(request, 'characters/detail.html', {
       'character': character,
       'story': story
    })


