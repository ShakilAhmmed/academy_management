from django.urls import path
from . import views
from . import category_views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('category/', category_views.category, name="category")
]
