from django.contrib import admin
# Import Django's admin module to register models for the admin interface

from .models import Conversation, ConversationMessage
# Import the models from this conversation app

admin.site.register(Conversation)
# Register the Conversation model with Django admin
# This allows admin users to view, create, edit, and delete conversations
# in the Django admin interface at /admin/
admin.site.register(ConversationMessage)
# Register the ConversationMessage model with Django admin  
# This allows admin users to view, create, edit, and delete individual messages
# in the Django admin interface