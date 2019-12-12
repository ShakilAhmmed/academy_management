from django.urls import path, include
from . import views
from . import courses_views

urlpatterns = [
    path('', courses_views.courses, name="courses"),

]
