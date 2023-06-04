from django.db import models
from django.urls import reverse


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'

  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'pokemon_id': self.id})


def __str__(self):
    return self.name

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )

  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"