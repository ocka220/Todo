from django.urls import path
from list_item.views import list_view, edit_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_view, name='list'),
    path('edit/<int:pk>', edit_view, name='edit'),
    # path('list/<int:pk>', list_view, name='list')
]