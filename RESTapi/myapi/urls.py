from django.urls import path

from . import views

urlpatterns = [
    path('/', views.overview , name="home"),
    path('/list', views.list_items, name='list-items'),
    path('/item/<str:pk>', views.item_datails,name='item-details'),
    path('/create/', views.create_item, name='create-item'),
    path('/item/<str:pk>/update/', views.update_item, name='update'),
    path('/item/<str:pk>/delete/', views.delete_item, name='delete')
]
