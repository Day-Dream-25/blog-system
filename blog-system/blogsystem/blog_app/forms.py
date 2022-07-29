from django.forms import ModelForm, forms
from blog_app.models import  Blog
from django import forms


class BlogForm(ModelForm):
    # description = forms.CharField(max_length=2000, widget=forms.Textarea(
    #                                attrs={
    #                                    'class': 'form-control',
    #                                    'cols': 80, 'rows': 18,
    #                                    'placeholder': 'you can write your story here ...'
    #                                }
    #                            )
    #                            )

    class Meta:
        model = Blog
        fields = ['user', 'title', 'image', 'Date', 'description']




