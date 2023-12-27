from django import forms

class CreateBlogForm(forms.Form):
    author = forms.CharField(label = 'author')
    title = forms.CharField(label = 'title')
    category = forms.CharField(label = 'category')
    content = forms.CharField(label = 'content')


class UpdateBlogForm(forms.Form):
    author = forms.CharField(label = 'author')
    title = forms.CharField(label = 'title')
    category = forms.CharField(label = 'category')
    content = forms.CharField(label = 'content')