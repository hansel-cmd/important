from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .forms import *
from .models import Blog, Favorite
from .utils.utils import get_path_referer
import math

# Create your views here.
class LoginView(View):
    def get(self, request):
        template = 'blog/login.html'
        context = {}

        if request.user.is_authenticated:
            return redirect('index')

        return render(request, template, context)

    def post(self, request):
        template = 'blog/login.html'
        context = {
            'values': request.POST
        }

        user = UserLoginForm(request.POST)
        valid, errors, user = user.check()

        if not valid:
            context['errors'] = errors
            return render(request, template, context)
        
        login(request, user)
        return redirect('index')


class SignupView(View):
    def get(self, request):
        template = 'blog/signup.html'
        context = {}
        return render(request, template, context)

    def post(self, request):
        template = 'blog/signup.html'
        context = {
            'values': request.POST
        }
        user = UserForm(request.POST)
        valid, errors = user.check()
        if not valid:
            context['errors'] = errors
            return render(request, template, context)
        user.save()
        return redirect('index')

def log_out(request):
    logout(request)
    return redirect('index')

@method_decorator(login_required(login_url='login'), name = 'dispatch')
class CreateView(View):
    def get(self, request):
        template = 'blog/create.html'
        return render(request, template)
    
    def post(self, request):
        updated_form = CreateBlogForm(request.POST)
        if updated_form.is_valid():
            blog = Blog(**{
                'user': request.user,
                'title': updated_form.cleaned_data['title'],
                'category': updated_form.cleaned_data['category'],
                'content': updated_form.cleaned_data['content'],
            })
            blog.save()
        return redirect('index')

@method_decorator(login_required(login_url='login'), name = 'dispatch')
class UpdateView(View):
    def get(self, request, id):
        template = 'blog/update.html'

        try:
            blog  = Blog.objects.get(pk = id, user__id = request.user.id)
        except Blog.DoesNotExist:
            return redirect('index')
        context = {
            'blog': blog
        }
        return render(request, template, context)

    def post(self, request, id):

        print(request.POST)
        updated_form = UpdateBlogForm(request.POST)
        if updated_form.is_valid():
            blog = Blog.objects.get(pk = request.POST['id'])
            blog.title = updated_form.cleaned_data['title']
            blog.category = updated_form.cleaned_data['category']
            blog.content = updated_form.cleaned_data['content']
            blog.save()
            return redirect('blog-details', id)
        return redirect('update', id)

@login_required(login_url='login')
def index(request):
    template = 'blog/index.html'
    
    per_page = 5
    try:
        page_number = int(request.GET.get('page'))
    except (ValueError, TypeError) as _:
        page_number = 1

    offset = page_number * per_page - per_page
    limit = page_number * per_page

    blogs = Blog.objects
    blogs = blogs.all().order_by('-created_at').prefetch_related('user')
    total = len(blogs)
    result = blogs[offset:limit]

    # Get the list of ids of the favorite blogs
    favorites = Favorite.objects.filter(user_id = request.user.id).values_list('blog_id', flat=True)

    context = {
        'favorites': favorites,
        'blogs': result,
        'page': page_number,
        'total': total,
        'range': range(1, math.ceil(total / per_page) + 1)
    }

    return render(request, template, context)

@login_required(login_url='login')
def blog_details(request, id):
    template = 'blog/blog-details.html'
    blog = get_object_or_404(Blog, pk = id)
    is_favorite = Favorite.objects.filter(blog_id = blog).exists()
    context = {
        'blog': blog,
        'is_favorite': is_favorite
    }
    return render(request, template, context)
        

def add_favorites(request, id):
    path = get_path_referer(request)
        
    try:
        # if it already exists in Favorite, unfavorite it
        blog = Favorite.objects.get(blog_id = id, user_id = request.user.id)
        blog.delete()
    except:
        # if it's not yet in Favorite, add it
        blog = Blog.objects.get(pk = id)
        favorite = Favorite(blog_id = blog, user_id = request.user)
        favorite.save()
    return redirect(path)
    
@login_required(login_url='login')
def favorites(request):
    template = 'blog/favorites.html'
    path = request.path

    per_page = 5
    try:
        page_number = int(request.GET.get('page'))
    except (ValueError, TypeError) as _:
        page_number = 1

    # Get all blogs that are in favorites
    blogs = Blog.objects.filter(favorite__isnull=False, favorite__user_id = request.user).order_by('-created_at')
    offset = page_number * per_page - per_page
    limit = page_number * per_page

    total = len(blogs)
    result = blogs[offset:limit]

    context = {
        'blogs': result,
        'page': page_number,
        'total': total,
        'range': range(1, math.ceil(total / per_page) + 1),
        'current_url': path
    }
    return render(request, template, context)


def delete(request, id):
    try:
        blog = Blog.objects.get(pk = id)
        blog.delete()
    except:
        pass
    return redirect('index')
        

