from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from .forms import CharacterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ['API_KEY']


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


@login_required
def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html',{
    'characters': characters
  })


def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, 'characters/detail.html', {
    'character': character,
    'story': character.story
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


class CharacterCreate(CreateView):
  model = Character
  form_class = CharacterForm
  template_name = 'main_app/characters_create.html'

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CharacterUpdate(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_update_form.html'
    success_url = '/characters'


class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters'



def character_story(request, character_id):
    character = Character.objects.get(id=character_id)

  
    openai.api_key = API_KEY
    
    prompt = f"Generate a short story about {character.name} in the Dark Souls universe, where they fight bosses, fight invaders, and link the first flame, in less than 500 characters"
    response = openai.Completion.create(
       engine="text-davinci-002",
       prompt=prompt,
       max_tokens=500,
       n=1,
       stop=None,
       temperature=0.7,
    )

    story = response.choices[0].text.strip()
    character.story = story
    character.save()

    return render(request, 'characters/detail.html', {
       'character': character,
       'story': story
    })


    