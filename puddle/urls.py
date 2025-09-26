"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" Import Django settings so we can serve media files during development
    Import Django admin site
    Import functions for defining URL patterns
    The main list of URL patterns for the project



"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Include all URLs from the 'core' app (homepage, etc.)
    path('', include('core.urls')),
    # Include all URLs from the 'item' app (for item-related pages)
    path('items/', include('item.urls')),
    # Include all URLs from the 'dashboard' app (user dashboard, profile, etc.)
    path('dashboard/', include('dashboard.urls')),
    # Include all URLs from the 'conversation' app (messaging/inbox system)
    path('inbox/', include('conversation.urls')),
    # Django’s built-in admin panel (accessible at /admin/)
    path('admin/', admin.site.urls),
# Serve uploaded media files (like images) during development
# This will map MEDIA_URL (e.g., '/media/') to MEDIA_ROOT (where files are stored)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
