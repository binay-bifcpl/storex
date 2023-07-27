from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
# your_project_name/urls.py

from django.contrib import admin
from lodin import views
from lodin.views import search_users

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
    path('search/', views.search_users, name='search_users'),
    path('store/', include('store.urls')),

]




