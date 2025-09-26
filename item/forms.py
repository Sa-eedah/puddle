from django import forms

from .models import Item
# Define a reusable CSS class string for consistent input styling
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
# Form for creating a new Item
class NewItemForm(forms.ModelForm):
    class Meta:
        # The form is based on the Item model
        model = Item
        # Fields that will appear in the form
        fields = ('category','name', 'description','price','image',)
        # Customize how form fields are rendered in HTML
        widgets = {
            # Dropdown for selecting category
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            # Input field for the item name
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            # Textarea for longer item descriptions
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            # Input field for price
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            # File input for uploading item image
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            }),     
        }

# Form for editing an existing Item
class EditItemForm(forms.ModelForm):
    class Meta:
        # The form is based on the Item model
        model = Item
        # Fields available when editing (includes is_sold toggle)
        fields = ('name', 'description','price','image','is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            }),     
        }