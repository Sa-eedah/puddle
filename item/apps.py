from django.apps import AppConfig

# Configuration class for the "item" app
class ItemConfig(AppConfig):
    # Sets the default type of primary key field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of the app this config applies to
    name = 'item'
