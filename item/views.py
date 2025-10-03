from django.contrib.auth.decorators import login_required  
from django.db.models import Q 
from django.shortcuts import render,get_object_or_404, redirect 

# Import custom forms and models from this app
from .forms import NewItemForm, EditItemForm
from  .models import Category, Item

"""To restrict access to logged-in users 
   To perform complex queries (OR, AND)
   Rendering templates, retrieving
"""

# Create your views here.
# -------------------------------
# View to list all items (with optional filtering & search)
# -------------------------------
def items(request):
    query = request.GET.get('query','') # Get search query string (?query=...)
    category_id = request.GET.get('category', 0) # Get category filter (?category=...)
    categories = Category.objects.all() # Retrieve all categories to display in filter options
    items = Item.objects.filter(is_sold=False) # Start with all unsold items

    if category_id:
        items = items.filter(category_id=category_id) # If a category filter is applied, narrow results



    if query: # If a search query is provided, filter by name OR description (case insensitive)
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

# Render items list page with context
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

# -------------------------------
# View to display details of a single item
# -------------------------------
def detail(request,pk):
    # Get the item or return 404 if not found
    item = get_object_or_404(Item, pk=pk)
    # Fetch up to 3 related items from the same category, excluding the current one
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    # Render item detail page
    return render(request, 'item/detail.html', { 
        'item': item, 
        'related_items': related_items
    })

# -------------------------------
# View to create a new item (restricted to logged-in users)
# -------------------------------

@login_required
def new(request):
    if request.method == "POST":
        # Bind form with POST data and uploaded files
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form but don’t commit yet (we need to set created_by)
            item = form.save(commit=False)
            item.created_by = request.user # Assign logged-in user
            item.save()

            return redirect('item:detail', pk=item.id) # Redirect to the detail page of the new item
    else:
# If GET request → show empty form
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item', # (❗️probably should say "New item")
    })

# -------------------------------
# View to edit an existing item (restricted to the creator only)
# -------------------------------

@login_required
def edit(request, pk):
    # Ensure the item exists and belongs to the current user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        # Pre-fill form with existing item data (instance=item)
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()  # Save updates

            return redirect('item:detail', pk=item.id)
    else:

        form = EditItemForm(instance=item) # If GET request → show form with item’s current values

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edited item',# (❗️probably should say "Edit item")
    })

# -------------------------------
# View to delete an item (restricted to the creator only)
# -------------------------------

@login_required
def delete(request, pk):
     # Only allow the owner of the item to delete it
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
# Redirect back to the user’s dashboard after deletion
    return redirect('dashboard:index')

