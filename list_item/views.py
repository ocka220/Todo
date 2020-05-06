from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


def edit_view(request, pk):
    pass


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
