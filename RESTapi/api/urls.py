from django.urls import path
from . import views

urlpatterns = [
    path("",views.getData),
    path("post",views.addItem),
    path("<str:pk>/del", views.deleteItem),
    path("<str:pk>/update", views.updateItem),
]
