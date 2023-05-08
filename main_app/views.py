from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Character
from .forms import CharacterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin









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
    'character': character
  })
  


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
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

    