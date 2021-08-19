from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm, UserLogin, UserLogup
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


  
class HomePost(ListView):
    template_name = 'news/index.html'
    context_object_name = 'post'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(HomePost, self).get_context_data(**kwargs)
        context.update({
            'category': Category.objects.all(),
        })
        return context


class CategoryPost(ListView):
    template_name = 'news/category.html'
    context_object_name = 'post'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['category_id'], is_published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['category'] = Category.objects.all()
        return context


class OnePost(DetailView):
    template_name = 'news/posts.html'
    context_object_name = 'post_all'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class Add_Post(CreateView):
    form_class = PostForm
    template_name = 'news/add_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class Update_Post(UpdateView):
    model = Post
    template_name = 'news/update_post.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class Delete_Post(DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class Log_IN(CreateView):
    form_class = UserLogin
    template_name = 'news/log_in.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

def log_up(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = UserLogup(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLogup()
    return render(request, 'news/log_up.html', {'category': category, 'form': form})

def log_out(request):
    logout(request)
    return redirect('log_in')
