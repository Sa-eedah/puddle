from django.contrib.auth.decorators import login_required
# Import decorator to require user login for accessing views
from django.shortcuts import render, get_object_or_404
# Import shortcuts for rendering templates and getting objects

# Create your views here.
# Import the Item model from the item app
from item.models import Item

# Decorator ensures only logged-in users can access this view
# If user is not logged in, they'll be redirected to login page
@login_required
def index(request):
    # Get all items that were created by the currently logged-in user
    # This filters the database to only show the user's own items
    items = Item.objects.filter(created_by=request.user)
    # Render the dashboard template and pass the user's items to it
    # The template can access these items using the 'items' variable
    return render(request,'dashboard/index.html', {
        'items':items, # Pass the filtered items to the template
    })


