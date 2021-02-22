from django import forms

from .models import Comments


class CommentPlayerForms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text',)
        labels = {'name': "Имя", 'text': "Комментарий"}
