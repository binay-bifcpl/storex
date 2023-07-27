# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_store_entry, name='add_store_entry'),
    # Add more URL patterns if needed.
    path('all/', views.all_entries, name='all_entries'),  # Add this line for displaying all entries.
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Add this line for editing an entry.
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),  # Add this line for deleting an entry.
    path('add_usage/', views.add_usage, name='add_usage'),  # Add this line for adding usage data.
    path('all_usage/', views.all_usage, name='all_usage'),  # Add this line for displaying all usage data.
    path('edit_usage/<int:usage_id>/', views.edit_usage, name='edit_usage'),  # Add this line for editing usage data.
    path('delete_usage/<int:usage_id>/', views.delete_usage, name='delete_usage'),
    path('download_usage/', views.download_usage_as_excel, name='download_usage'),  # Add this line for downloading usage data as Excel.
    path('download_store_entries/', views.download_store_entries_as_excel, name='download_store_entries'),  # Add this line for downloading store entries as Excel.
]
# store/urls.py


