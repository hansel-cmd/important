from django import forms

class UpdateTodoForm(forms.Form):

    title = forms.CharField(label = 'title', max_length = 200)
    is_completed = forms.BooleanField(label = 'is_completed')