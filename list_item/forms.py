from list_item.models import ListItemModel
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class ListItemForm(forms.ModelForm):
    """
    Форма натсроек расписания обмена
    """
    name = forms.CharField(required=True, widget=forms.TextInput())

    class Meta:
        model = ListItemModel
        fields = ('name', 'expire_date')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }


