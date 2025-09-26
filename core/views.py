from django.shortcuts import render, redirect

from item.models import Category, Item # Import models from the item app

from .forms import SignupForm # Import the custom signup for

# Create your views here.
"""Homepage"""
def index(request):
    # Get the first 6 items that are not sold
    items = Item.objects.filter(is_sold=False)[0:6]
    # Get all available categories
    categories = Category.objects.all()
    # Render the homepage template with categories and items as context
    return render(request, 'core/index.html', {'categories':categories, 'items': items,})

# View for the contact page
def contact(request):
    # Simply render the contact template
    return render(request, 'core/contact.html')

# View for the signup page
def signup(request):
    # If the form is submitted with POST request
    if request.method == 'POST':
        # Bind form with POST data
        form = SignupForm(request.POST)
# If the form is valid, save the user to the database
        if form.is_valid():
            form.save()
# Redirect to the login page after successful signup
        return redirect('/login/')
    
    else:
        # If GET request, display an empty signup form
        form = SignupForm
# Render the signup template with the form
    return render(request, 'core/signup.html', {
        'form':form
    })
