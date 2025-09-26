from django.apps import AppConfig
# Import Django's AppConfig class for app configuration

# Configuration class for the dashboard app
class DashboardConfig(AppConfig):
    # Set the default field type for primary keys in models
    # BigAutoField creates auto-incrementing ID fields that can handle large numbers
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of this Django app
    # This should match the folder name of your app
    name = 'dashboard'
