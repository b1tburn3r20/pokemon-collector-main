from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {
    'pokemon': pokemon
  })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  # First, create a list of the item ids that the pokemon DOES have
  id_list = pokemon.items.all().values_list('id')
  # Query for the items that the pokemon doesn't have
  # by using the exclude() method vs. the filter() method
  items_pokemon_doesnt_have = Item.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  feeding_form = FeedingForm()
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form,
    'items': items_pokemon_doesnt_have
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'breed', 'description', 'age']

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['breed', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon'

def add_feeding(request, pokemon_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # pokemon_id FK.
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('detail', pokemon_id=pokemon_id)

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items'

def assoc_item(request, pokemon_id, item_id):
  Pokemon.objects.get(id=pokemon_id).items.add(item_id)
  return redirect('detail', pokemon_id=pokemon_id)

def unassoc_item(request, pokemon_id, item_id):
  Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
  return redirect('detail', pokemon_id=pokemon_id)
