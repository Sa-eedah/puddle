from django.contrib.auth import views as auth_views
# Import Django's built-in authentication views (like LoginView, LogoutView, etc.)
# Import path function for defining URL patterns
from django.urls import path
# Import views from the current app (the local views.py file)
from . import views
# Import custom LoginForm from the forms module in this app
from .forms import LoginForm

app_name = 'core'
# Define the app namespace - this allows you to reference URLs as 'core:index', 'core:login', etc.

# List of URL patterns for this app
urlpatterns = [
    # Root URL ('') maps to the index view function
    # Name 'index' allows reverse URL lookup with {% url 'core:index' %} in templates
    path('', views.index, name='index'),
    # '/contact/' URL maps to the contact view function
    # Accessible as {% url 'core:contact' %} in templates
    path('contact/', views.contact, name='contact'),
    # '/signup/' URL maps to the signup view function
    # Handles user registration, accessible as {% url 'core:signup' %}
    path('signup/', views.signup, name='signup'),
    # '/login/' URL uses Django's built-in LoginView class-based view
    # Configured with custom template 'core/login.html' and custom LoginForm
    # The authentication_form parameter overrides the default login form
    # Accessible as {% url 'core:login' %} in templates
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'), # Custom template for login page
    # Custom form class for authentication
]
