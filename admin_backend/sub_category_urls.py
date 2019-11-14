from django.urls import path, include
from . import views
from . import sub_category_views

urlpatterns = [
    path('', sub_category_views.sub_category, name="sub_category"),

]
