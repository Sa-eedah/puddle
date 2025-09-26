from django.urls import path
#Import path function to define URL patterns

from . import views
# Import views from this app (dashboard/views.py)

app_name = 'dashboard'
# Set the app namespace to 'dashboard'
# This lets you reference URLs as 'dashboard:index' in templates and code

# List of URL patterns for the dashboard app
urlpatterns = [
    # Empty path ('') means this is the main dashboard page
    # Maps to the index view function in views.py
    # Can be accessed in templates as {% url 'dashboard:index' %}
    path('', views.index, name='index'),
]
