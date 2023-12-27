from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .models import *
from .forms import *

class LoginView(View):
    def get(self, request):
        template = 'todos/login.html'
        context = {
            'errors': {}
        }

        if request.user.is_authenticated:
            return redirect('index')
        return render(request, template, context)

    def post(self, request):
        template = 'todos/login.html'
        context = {
            'values': request.POST
        }

        user = UserLoginForm(request.POST)
        credentials = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password'),
        }
        valid, errors, user = user.check()
        # user = authenticate(**credentials)
        print('HAAHAHAHAHA', valid, errors, user)
        
        if not valid:
            context['errors'] = errors
            return render(request, template, context)

        login(request, user)
        return redirect('index')


class SignUpView(View):
    def get(self, request):
        template = 'todos/signup.html'
        context = {
            'errors': {}
        }

        if request.user.is_authenticated:
            return redirect('index')
        return render(request, template, context)

    def post(self, request):
        template = 'todos/signup.html'
        context = {
            'values': request.POST
        }

        print(request.POST)
        user = UserForm(request.POST)
        
        valid, errors = user.check()
        if not valid:
            print("INVALID", valid)
            context['errors'] = errors
            return render(request, template, context)
        
        user.save()
        print("HELLO")
        return redirect('login')

# @cache_page(900)
@login_required(login_url="login")
def index(request):
    template = 'todos/index.html'
    todos = ToDo.objects.filter(user__id = request.user.id)
    
    context = {
        'tab': 'ALL',
        'todos': todos
    }

    response = render(request, template, context)

    # Doesnt matter
    if request.COOKIES.get('visits'):
        visits = request.COOKIES.get('visits')
        visits = int(visits) + 1
        response.set_cookie('visits', str(visits))
    else:
        response.set_cookie('visits', '1')

    return response

@login_required(login_url="login")
def pending(request):
    template = 'todos/index.html'
    todos = ToDo.objects.filter(is_completed = False, user__id = request.user.id)
    context = {
        'tab': 'PENDING',
        'todos': todos
    }
    return render(request, template, context)

@login_required(login_url="login")
def completed(request):
    template = 'todos/index.html'
    todos = ToDo.objects.filter(is_completed = True, user__id = request.user.id)
    context = {
        'tab': 'COMPLETED',
        'todos': todos
    }
    return render(request, template, context)

def update_completed(request):
    todo = ToDo.objects.get(pk = request.POST.get('id'))
    if request.POST.get('is_completed') == 'true':
        todo.is_completed = True
    else:
        todo.is_completed = False
    todo.save()
    return redirect('index')


UpdateTodoForm = modelform_factory(ToDo, exclude = [])
def add(request):
    updated_form = UpdateTodoForm({
        'title': request.POST.get('title'),
        'is_completed': False,
        'user': request.user.id
    })
    if updated_form.is_valid():
        updated_form.save()

    return redirect('index')

@require_http_methods(['DELETE'])
@csrf_exempt # use to bypass the required csrf_token in a form when using postman
def delete(request):
    query_dict = QueryDict(request.body)
    print("HAHAAHAHAHAHHAHAHAHAHH")
    print(query_dict)
    ToDo.objects.filter(pk = query_dict.get('id')).delete()
    return redirect('index')

def log_out(request):
    print(request.session)
    logout(request)
    return redirect('index')


@method_decorator(csrf_exempt, name = 'dispatch')
class MyTestView(View):
    def get(self, request):

        # Implement log in
        # If user exists, set to session
        # otherwise, return to log in page. Needs to log in.
        name = 'Katarina'
        id = 1234124
        if not request.session.has_key('customer'):
            request.session['customer'] = name
            print("SESSION VALUE SET!!!!!!!!!!!!")        

        return render(request, "todos/test.html")
    
    @csrf_exempt
    def post(self, request):
        return HttpResponse("POST REQUEST HANDLED BY MyTestView")
    
    @csrf_exempt
    def delete(self, request):
        return HttpResponse("DELETE REQUEST HAHNDLED BY MyTestView")
    

"""
Session Demo
"""

# def login(request):
#     name = 'WINTER'
#     id = 98713

#     if not request.session.has_key('aespa'):
#         request.session['aespa'] = name
#         print("SESSION VALUE SET!!!!!!!!!!!!")

#     return HttpResponse(f"Hello, {request.session['aespa']}!")

# def log_out(request):
#     try:
#         del request.session['aespa']
#     except KeyError:
#         print("1. error happened.")

#     try:
#         del request.session['customer']
#     except KeyError:
#         print("2. error happened.")

#     return HttpResponse("Log out...")