from django import forms
from django.core.exceptions import ValidationError


class FruitsForm(forms.Form):
    id = forms.IntegerField(
        label="ID", 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "form-control", "name": "id"})
        )

    name = forms.CharField(
        label='果実名',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "name": "fruits_name"})
        )

    memo = forms.CharField(
        label='メモ', 
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "name": "memo"})
        )


    def clean_id(self):
        value = self.cleaned_data['id']
        if value is None:
            raise forms.ValidationError('{0}を入力してください。'.format('ID'))
        elif value < 1:
            raise forms.ValidationError('{0}を入力してください。'.format('ID'))

    def clean_name(self):
        value = self.cleaned_data['name']
        if value == '':
            raise forms.ValidationError('{0}を入力してください。'.format('果実名'))
        elif not 0 < int(len(value)) < 10:
            raise forms.ValidationError('{0}を{1}文字以内で入力してください。'.format('果実名', 10))

    def clean_memo(self):
        value = self.cleaned_data['memo']
        if value != '' and not 5 < int(len(value)) < 50:
            raise forms.ValidationError('{0}は{1}～{2}文字で入力してください。'.format('メモ', 5, 50))


