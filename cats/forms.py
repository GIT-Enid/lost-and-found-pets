
from django import forms
from .models import CatPost, Comment

class CatPostForm(forms.ModelForm):
    class Meta:
        model = CatPost
        fields = ['image', 'title', 'description', 'location', 'status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
