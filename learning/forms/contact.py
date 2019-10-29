from django import forms
from learning.models import Product

class Contact(forms.Form):
    name = forms.CharField(
        label='isim',
        max_length=50,
        min_length=5,
        required=True,
        initial='isminizi giriniz...',
        help_text='burası isim yardım metnidir',
        error_messages= {
            'required': 'lütfen isim giriniz',
            'max_length': 'En fazla 5o karakter girebilirsiniz',
            'min_length': 'En az 5 karakter girmelisiniz'
        },
        disabled=False,
        widget=forms.TextInput(
            attrs= {
                'class': 'special',
                'size': '40',
                'title': 'İsminiz',
                'required': True
            }
        )
    )

    email = forms.EmailField(label='Email adresi')
    content = forms.CharField(widget=forms.Textarea)
