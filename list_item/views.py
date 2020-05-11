from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from list_item.forms import ListItemForm
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

PAGE_COUNT = 6


@login_required(login_url='registration/login/')
def list_view(request, pk):
    user = request.user

    lists = ListItemModel.objects.filter(list_id=pk).order_by('-created')
    list_name = get_object_or_404(ListModel, id=pk, user_id=user.id)

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
        'user': request.user.username,
        'list_name': list_name,
        'pages': list(paginator.page_range)

    }
    return render(request, 'list.html', context)


def edit_list_item_view(request, pk):
    list_item = ListItemModel.objects.filter(id=pk).first()
    list_id = list_item.list_id

    if request.method == 'POST':
        form = ListItemForm({
            'name': request.POST['name'],
            'expire_date': request.POST['expire_date'],
            'list': list_id,
        }, instance=list_item)
        success_url = reverse('list_item:list', kwargs={'pk': list_id})

        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = ListItemForm(instance=list_item)

    return render(request, 'edit_list_item.html', {'form': form, 'pk': list_id})



@login_required(login_url='registration/login/')
def create_item_view(request, pk):
    form = ListItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        expire_date = request.POST['expire_date']
        form = ListItemForm({
            'name': name,
            'expire_date': expire_date,
            'list': pk,
        })
        success_url = reverse('list_item:list', kwargs={'pk': pk})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list_item.html', {'form': form, 'pk': pk})


def done_view(request):

    data = json.loads(request.body.decode())
    pk = int(data['id'])
    list_item = ListItemModel.objects.get(id=pk)
    value = not list_item.is_done
    list_item.is_done = value
    list_item.save()
    return HttpResponse(status=201)