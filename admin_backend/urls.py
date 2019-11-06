from django.urls import path, include
from . import views
from . import category_views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('category/', include('admin_backend.category_api')),
]
