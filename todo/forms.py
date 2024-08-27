# todo/forms.py

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': '今天要做什麼事??', 'class': 'form-control'}),
        }
