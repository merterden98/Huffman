from django import forms


class TestForm(forms.Form):

    data = forms.CharField(max_length=100,widget=forms.TextInput(attrs={

        'class' : 'form-control'

    }))