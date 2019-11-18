from django.urls import path, include
from . import views
from . import category_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', category_views.category, name="category"),
    path('add_category', login_required(category_views.CategoryApi.as_view()), name="add_category"),
    path('category_detail/<int:pk>', login_required(category_views.CategoryDetail.as_view()), name="category_detail"),
    path('category_status/<int:pk>', login_required(category_views.CategoryStatus.as_view()), name="category_status"),
]
