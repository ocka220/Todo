from django.shortcuts import render, redirect
from django.urls import reverse

from main.forms import ListForm
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

    # set1 = lists.filter(name='Работа') - доп.ветвление на основной фильтр

    context = {
        'lists':lists,
        'user': user.username
    }

    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'


def create_view(request):
    """view создания нового списка"""

    form = ListForm()

    if request.method == 'POST':
        name = request.POST['name']
        form = ListForm({
            'name': name,
            'user': request.user
        })
        success_url = reverse('main:main')
        user = request.user

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})


