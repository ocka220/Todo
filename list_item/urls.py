from django.urls import path
from list_item.views import list_view, create_item_view, edit_list_item_view, done_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_view, name='list'),
    path('edit/<int:pk>', edit_list_item_view, name='edit'),
    path('create/<int:pk>', create_item_view, name='create'),
    # path('delete/', delete_view, name='delete'),
    path('done/', done_view, name='done'),
]
