from django.urls import path, include
from . import views
from . import views

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('admin_logout', views.logout_staff_admin, name="admin_logout"),

]
