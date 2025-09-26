from django.apps import AppConfig
# Import Django's AppConfig class for app configuration

# Configuration class for the conversation app
# This app handles messaging/chat functionality between users
class ConversationConfig(AppConfig):
    # Set the default field type for primary keys in models
    # BigAutoField creates auto-incrementing ID fields that can handle large numbers
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of this Django app
    # This should match the folder name of your app ('conversation')
    name = 'conversation'
