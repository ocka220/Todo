from django.shortcuts import render

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# user = User('Bob', 23)

data = {
    'lists': [
        {'id': 1, 'name': 'Работа', 'is_done': True},
        {'id': 2, 'name': 'Дом', 'is_done': False},
        {'id': 3, 'name': 'Учеба', 'is_done': True}
    ],
    'user_name': 'Admin',
}


# for list in data ['lists']:
#     name = lists[0]
#       is_done = list[1]

# Create your views here.
def main_view(request, pk=0):
    context = data
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'
