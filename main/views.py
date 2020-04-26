from django.shortcuts import render
from main.models import ListModel


# data = {
#     'lists': [
#         {'id': 1, 'name': 'Работа', 'is_done': True},
#         {'id': 2, 'name': 'Дом', 'is_done': False},
#         {'id': 3, 'name': 'Учеба', 'is_done': True}
#     ],
#     'user_name': 'Admin',
# }


def main_view(request):
    """главная view"""
    user = request.user

    lists = ListModel.objects.filter(
        user=user).order_by('created')
    # lists = ListModel.objects.filter(user_id=user_id)
    # user.username
    # user.email
    context = {
        'lists':lists,
        'user': user.username
    }

    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'


def new_list_view(request):
    """view создания нового списка"""

    return render(request, 'new_list.html')

