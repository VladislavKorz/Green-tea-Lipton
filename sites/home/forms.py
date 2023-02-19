
from django import forms

class ContactForm(forms.Form):
    ROLS_CHOISE = ((
        'HR', 'HR'),
        ('support', 'Поддержка сайта'),
        ('manager', 'Руководитель'))
    from_email = forms.EmailField(label='От')
    to_email = forms.ChoiceField(choices=ROLS_CHOISE, label='Кому')
    title = forms.CharField(label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')