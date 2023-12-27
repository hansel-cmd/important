from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.contrib.auth import authenticate


class UpdateTodoForm(forms.Form):

    title = forms.CharField(label = 'title', max_length = 200)
    is_completed = forms.BooleanField(label = 'is_completed')


class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]

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

    confirm_password = forms.CharField(label = 'confirm_password', max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password']

    def is_unique(self, username):
        try:
            User.objects.get(username = username)
            return False
        except User.DoesNotExist:
            return True

    def match(self, this, other):
        return this == other
    
    def alpha(self, string):
        if string == None:
            return False
        
        if any(not x.isalpha() for x in string):
            return False
        return True
    
    def check(self):
        username = self.data.get('username')
        firstname = self.data.get('first_name')
        lastname = self.data.get('last_name')
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')

        print('aaaaaaa', firstname, lastname, username, password)

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

        if not self.alpha(firstname):
            valid = False
            errors['firstname'] = {
                'error_msg': 'First Name must be in the alphabets.'
            }
        
        if not self.alpha(lastname):
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
        
        return  valid, errors
    
    def save(self, commit = True):
        m = super().save(commit = False)
        m.username = self.cleaned_data['username']
        m.password = make_password(self.cleaned_data['password'])
        
        if commit:
            m.save()
        return m
        