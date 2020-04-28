from django.db import models


class ListItemModel(models.Model):
    """ Модель списка дел """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    listmodel = models.ForeignKey('main.ListModel', on_delete=models.CASCADE, verbose_name='Список дел')
    is_done = models.BooleanField(default=False)
    expare_data = models.DateField(blank=True, null=True)
    priority = models.SmallIntegerField(verbose_name='Приоритет', default=0)

    class Meta:
        verbose_name = 'Элемент списка'