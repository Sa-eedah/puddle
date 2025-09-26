from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    # Category name
    name = models.CharField(max_length=255)

    class Meta:
         # Sort categories alphabetically by name when queried
        ordering = ('name',)
        # Change plural display name in Django Admin from "Categorys" to "Categories"
        verbose_name_plural = 'Categories'

    def __str__(self):
        # Display category name when the object is printed (e.g., in admin)
        return self.name

class Item(models.Model):
    # Each item belongs to a category
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # Item's name
    name = models.CharField(max_length=255)
    # Description of item
    description = models.TextField(blank=True, null= True)
    # Price of Item
    price = models.FloatField()
    # Optional image upload (stored in 'media/item_images/')
    image = models.ImageField(upload_to='item_images', blank=True, null= True)
    # Boolean flag to mark if the item is already sold
    is_sold = models.BooleanField(default=False)
    # Link the item to the user who created it
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    # Automatically store the date and time when the item was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display the item name when the object is printed (e.g., in admin)
        return self.name

    
