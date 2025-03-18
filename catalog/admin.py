from django.contrib import admin
from .models import Cat, Breed, Picture

# Register your models here.

admin.site.register(Cat)
admin.site.register(Breed)
admin.site.register(Picture)