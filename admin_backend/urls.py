from django.urls import path, include
from . import views
from . import category_views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('category/', include('admin_backend.category_api')),
    path('sub_category/', include('admin_backend.sub_category_urls')),
    path('courses/', include('admin_backend.courses_urls')),
]
