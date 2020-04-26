from django.shortcuts import render

from list_item.models import ListItemModel
from main.models import ListModel

# data = {
#     'lists': [
#         {'id':1, 'name': 'Купить шариков', 'is_done': True, 'date': "25.04.20"},
#         {'id':2, 'name': 'Заказать торт', 'is_done': False, 'date': "15.04.20"},
#         {'id':3, 'name': 'Разослать приглашения', 'is_done': True}
#     ],
#     'user_name': 'Admin',
# }

def list_view(request, pk):
    #user = request.user

    lists = ListItemModel.objects.filter(listmodel_id=pk).order_by('created')
    name = ListModel.objects.filter(id=pk).first()
    context = {
        'lists': lists,
        'user': request.user.username,
        'name': name
    }
    return render(request, 'list.html', context)


def edit_view(request, pk):
    return 'Hello'


