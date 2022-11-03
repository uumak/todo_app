from django import forms
from .models import TodoApp

class TodoAppsform(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = [
            "title",
            "description",
        ]