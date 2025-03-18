from django.db import models

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

class Breed(models.Model):
    """Model representing a cat's breed"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a cat breed (e.g. Siamese, Maine Coon, British Shorthair, Moggie, etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular breed."""
        return reverse('breed-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='breed_name_case_insensitive_unique',
                violation_error_message = "Breed already exists (case insensitive match)"
            ),
        ]

class Cat(models.Model):
    """Model representing a cat."""
    title = models.CharField(max_length=200,
                             help_text='Made up nickname for the cat when we do not know its actual name')

    description = models.TextField(max_length=1000, 
                                   help_text="Enter a brief description of the cat")

   
    # Foreign Key used because a cat can only have one breed, but breeds can have multiple cats.
    breed = models.ForeignKey('Breed', 
                              on_delete=models.RESTRICT, 
                              null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this cat."""
        return reverse('cat-detail', args=[str(self.id)])
    
    
class Picture(models.Model):
    title = models.CharField(max_length=200,
                             null=True)

    description = models.TextField(
        max_length=1000, help_text="Enter a brief description of the image")
    
    image = models.ImageField(upload_to='cat_images')
    
    # Foreign Key used because a picture can only be of one cat, but cats can have multiple pictures.
    cat = models.ForeignKey('Cat', on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
