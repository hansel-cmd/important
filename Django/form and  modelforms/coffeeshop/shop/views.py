from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .utils import *
from .models import Coffee
from .forms import NameForm, UserForm, UserDetailForm

# Create your views here.
def home(request):
    template = 'shop/home.html'
    return render(request, template)

def complete(request):
    template = 'shop/complete.html'
    return render(request, template)

def sign_up(request):
    template = 'shop/signup.html'
    context = {
        'form': UserForm(initial={'email': '@gmail.com'})
    }
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # will be saved in a session
            # request.user
            login(request, user)
            return redirect('details')
        context['form'] = form

    return render(request, template,  context)

def details(request):
    template = 'shop/details.html'
    context = {
        'form': UserDetailForm(initial={
            'username': request.user.username,
            'email': request.user.email
        })
    }

    if request.method == 'POST':
        # Will run all validators defined/available in the UserDetailForm()
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complete')
        else:
            print("NO WAY!")
        
        context['form'] = form
    return render(request, template, context)

def place_order(request):
    template = 'shop/order.html'
    OrderFormSet = modelformset_factory(Coffee, fields = [
        'name', 'size', 'quantity'
    ], max_num=3, extra=3, can_delete=True, validate_max=True)

    
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home')
        else:
            print("NOP")
    else:
        data = {
            'form-TOTAL_FORMS': '3',
            'form-INITIAL_FORMS': '0',
            'form-0-name': AMERICANO,
            'form-0-size': LARGE,
            'form-0-quantity': '1',
            'form-0-name': CAPPUCCINO,
            'form-0-size': LARGE,
            'form-0-quantity': '1',
            'form-0-name': COLD,
            'form-0-size': LARGE,
            'form-0-quantity': '1',

        }
        order_formset = OrderFormSet(data, queryset=Coffee.objects.none())
    return render(request, template, {'formset': order_formset})