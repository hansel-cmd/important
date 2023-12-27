from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# from .models import User
from .models import UserDetail


class NameForm(forms.Form):

    name = forms.CharField(label = 'Your name', max_length=200)

    def save(self):
        pass


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # altenative: fields = "__all__"
        fields = ['username', 'password', 'email']

        # Override default error messages returned by validators
        error_messages = {
            'username': {
                'unique': _("Please enter another username. This one is taken.")
            },
        }

    # Saves to the database if commit is True
    def save(self, commit = True, *args, **kwargs):
        
        # commit = False, so it wont save to the database yet
        m = super().save(commit = False)
        m.username = self.cleaned_data['username']
        m.password =  make_password(self.cleaned_data['password'])
        print(m)
        if commit:
            m.save()
        
        return m
    

class UserDetailForm(forms.ModelForm):
    last_name = forms.CharField(required=False)
    class Meta:
        model = UserDetail
        fields = "__all__"
        
        # Override default error messages returned by validators
        error_messages = {
            'address': {
                'invalid_address': _("Wrong address format. It should not contain numbers.")
            }
        }

    """
    Alternative from adding a validators in the Model,i.e.,
    zipcode = models.CharField(max_length=4, validators=[test_zipcode(10)])

    It has to start with clean_<property>(self).

    It runs when instantiating UserDetailForm() but before calling is_valid().
    """
    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')
        if len(zipcode) != 4:
            raise forms.ValidationError("Zipcode needs to be of length 4")
        return zipcode
    

    """
    You may also add form level error by overriding clean() method.

    clean will run after form = UserDetailForm(request.POST) in the views, but
    before is_valid() is called.
    """
    def clean(self):
        zipcode = self.cleaned_data['zipcode']
        if zipcode != '1234':
            # this raises a field level error
            self.add_error('zipcode', 'We only deliver at zipcode 1234.')

            # this raises a form level error
            raise forms.ValidationError(_("There is something wrong with your input."))
        
    """
    Catches all the errrors if there is any.
    calling super().is_valid() checks if there is an error in the form and returns False
    if there is.
    """
    def is_valid(self) -> bool:
        print("VALIDATING FIELDS...")
        return super().is_valid()