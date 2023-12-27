from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import User

class CreateBlogForm(forms.Form):
    title = forms.CharField(label = 'title')
    category = forms.CharField(label = 'category')
    content = forms.CharField(label = 'content')


class UpdateBlogForm(forms.Form):
    title = forms.CharField(label = 'title')
    category = forms.CharField(label = 'category')
    content = forms.CharField(label = 'content')


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def check(self):
        username = self.data.get('username', None)
        password = self.data.get('password', None)

        errors = {
            'username': {},
            'password': {}
        }

        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            errors['username'] = {
                'error_msg': "The user does not exist."
            }
            return False, errors, None

        user = authenticate(**{'username': username, 'password': password})
        if not user:
            errors['password'] = {
                'error_msg': "Wrong password."
            }
            return False, errors, user
        
        return True, errors, user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password']

    def is_unique(self, username):
        try:
            User.objects.get(username = username)
            return False
        except User.DoesNotExist:
            return True
    
    def alpha(self, string):
        if string == None:
            return False
        
        if any(not x.isalpha() for x in string):
            return False
        return True
    
    def match(self, this, other):
        return this == other
    
    def check(self):
        username = self.data.get('username')
        email = self.data.get('email')
        last_name = self.data.get('last_name')
        first_name = self.data.get('first_name')
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')

        valid = True
        errors = {
            'username': {},
            'email': {},
            'firstname': {},
            'lastname': {},
            'password': {},
            'confirm_password': {}
        }

        if not self.is_unique(username):
            valid = False
            errors['username'] = {
                'error_msg': 'Username is already taken.'
            }

        if not self.alpha(first_name):
            valid = False
            errors['firstname'] = {
                'error_msg': 'First Name must be in the alphabets.'
            }
        
        if not self.alpha(last_name):
            valid = False
            errors['lastname'] = {
                'error_msg': 'Last Name must be in the alphabets.'
            }

        if not self.match(password, confirm_password):
            valid = False
            errors['password'] = {
                'error_msg': 'Password and Confirm Password does not match.'
            }
            errors['confirm_password'] = {
                'error_msg': 'Password and Confirm Password does not match.'
            }

        return valid, errors
    
    def save(self, commit = True):
        m = super().save(commit = False)
        m.username =  self.cleaned_data['username']
        m.password = make_password(self.cleaned_data['password'])

        if commit:
            m.save()
        return m