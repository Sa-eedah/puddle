from django.contrib import admin

# Register your models here.
# Import the models from this app
from .models import Category, Item
# Register the Category model with the Django admin site
# This makes Category objects manageable through the admin dashboard
admin.site.register(Category)
# Register the Item model with the Django admin site
# This makes Item objects manageable through the admin dashboard
admin.site.register(Item)