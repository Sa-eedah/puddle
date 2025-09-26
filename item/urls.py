from django.urls import path

from . import views
#: The namespace for this app's URLs.
app_name = 'item'

#: URL patterns for the item app.
#: Each pattern maps a URL path to its corresponding view.
urlpatterns = [
    path('', views.items, name='items'),
    # Displays a list of items or handles search queries.
    path('new/', views.new, name='new'),
    # Allows users to create a new item.
    path('<int:pk>/', views.detail, name='detail'),
    # Shows detailed information about a single item (by primary key).
    path('<int:pk>/delete/', views.delete, name='delete'),
    # Deletes the specified item (by primary key).
    path('<int:pk>/edit/', views.edit, name='edit'),
    # Allows editing the specified item (by primary key).
]
