from django.urls import path, include
from . import views
from . import category_views

urlpatterns = [
    path('', category_views.category, name="category"),
    path('add_category', category_views.CategoryApi.as_view(), name="add_category")
]