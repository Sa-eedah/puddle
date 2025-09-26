from django.urls import path

from . import views

# Set the app namespace to 'conversation'
# This lets you reference URLs as 'conversation:inbox', 'conversation:detail', etc.
app_name = 'conversation'
# List of URL patterns for the conversation app
urlpatterns = [
    # Empty path ('') shows the user's inbox with all their conversations
    # Example: /conversation/
    # Maps to inbox view - accessible as {% url 'conversation:inbox' %}
    path('', views.inbox, name='inbox'),
     # URL with conversation ID to view a specific conversation
    # Example: /conversation/5/ (where 5 is the conversation ID)
    # Maps to detail view - accessible as {% url 'conversation:detail' pk=conversation.id %}
    path('<int:pk>/', views.detail, name='detail'),
     # URL to start a new conversation about a specific item
    # Example: /conversation/new/3/ (where 3 is the item ID)
    # Maps to new_conversation view - accessible as {% url 'conversation:new' item_pk=item.id %}
    path('new/<int:item_pk>/', views.new_conversation, name='new'),

]
