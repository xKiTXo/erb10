
from django.urls import path,include
from . import views
app_name="chefs"
urlpatterns = [
    path('', views.index,name="index"),
]
