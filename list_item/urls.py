from django.urls import path
from list_item.views import list_view

app_name = 'list_item'

urlpatterns = [
    path('', list_view, name='list_item'),
]