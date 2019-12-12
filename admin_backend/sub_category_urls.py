from django.urls import path, include
from . import views
from . import sub_category_views

urlpatterns = [
    path('', sub_category_views.sub_category, name="sub_category"),
    path('delete/<int:pk>', sub_category_views.sub_category_delete, name="sub_category_delete"),
    path('status/<int:pk>', sub_category_views.sub_category_status, name="sub_category_status"),
    path('edit/<int:pk>', sub_category_views.sub_category_edit, name="sub_category_edit")

]
