from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon


pokemon = [
  {'name': 'Pikachu', 'type': 'electric', 'description': 'pika pika type shit', 'age': 5},
  {'name': 'Oshawott', 'type': 'water', 'description': 'cute fr', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
   return render(request, 'about.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all() # Retrieve all 

  # We pass data to a template very much like we did in Express!
  return render(request, 'pokemon/index.html', {
    'pokemon': pokemon
  })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', { 'pokemon': pokemon })



class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  # Special string pattern Django will use
  success_url = '/pokemon/{pokemon_id}' # <--- must specify an exact ID
  # Or...more fitting... you want to just redirect to the index page
  # success_url = '/pokemon'
class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a pokemon by excluding the name field!
  fields = ['breed', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon'
