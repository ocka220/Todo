from django.urls import path
from list_item.views import list_view, edit_view, create_item_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_view, name='list'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('create/<int:pk>', create_item_view, name='create')
]
