from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import  login_required
from main.forms import ListForm
from main.models import ListModel
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# data = {
#     'lists': [
#         {'id': 1, 'name': 'Работа', 'is_done': True},
#         {'id': 2, 'name': 'Дом', 'is_done': False},
#         {'id': 3, 'name': 'Учеба', 'is_done': True}
#     ],
#     'user_name': 'Admin',
# }

PAGE_COUNT = 6


@login_required(login_url='registration/login/')
def main_view(request):
    """главная view"""
    user = request.user

    lists = ListModel.objects.filter(
        user=user).order_by('-created')

    # lists = ListModel.objects.filter(user_id=user_id)
    # user.username
    # user.email

    # set1 = lists.filter(name='Работа') - доп.ветвление на основной фильтр


    paginator = Paginator(lists, PAGE_COUNT)
    page = request.GET.get('page')

    try:
        list_page = paginator.page(page)
    except PageNotAnInteger:
        list_page = paginator.page(1)
    except EmptyPage:
        list_page = paginator.page(paginator.num_pages)

    context = {
        'lists': list_page,
        'user': user.username,
        'pages': list(paginator.page_range)
    }

    return render(request, 'index.html', context)


@login_required(login_url='registration/login/')
# def edit_view(request, pk):
#
#     """view редактирования списка"""
#     form = ListForm()
#     list = ListModel.objects.get(id=pk)
#
#     if request.method == 'POST':
#         list.name = request.POST.get['name']
#         form = ListForm({
#                     'name': name,
#                     'user': request.user
#                 })
#         success_url = reverse('main:main')
#
#         if form.is_valid():
#                 form.save()
#                 return redirect(success_url)
#
#     else:
#         return render(request, 'new_list.html', {'list': list})



@login_required(login_url='registration/login/')
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



