from main.models import ListModel
from django import forms


class ListForm(forms.ModelForm):
    """
    Форма натсроек расписания обмена
    """
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')