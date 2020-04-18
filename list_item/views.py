from django.shortcuts import render

data = {
    'lists1': [
        {'name': 'Купить шариков', 'is_done': True, 'date': "25.04.20"},
        {'name': 'Заказать торт', 'is_done': False, 'date': "15.04.20"},
        {'name': 'Разослать приглашения', 'is_done': True}
    ],
    'user_name': 'Admin',
}


# Create your views here.
def list_view(request):
    context = data
    return render(request, 'list.html', context)
