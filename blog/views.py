from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

'''
this is function based view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
Class based view are better than function base as you see
'''


def about(request):
    return render(request, 'blog/about.html', {'title': "About Author"})


class PostListView(ListView):
    # this is class based view djang0 support few of them like ListView , DetailView, delete update etc
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'  # what variable posts ll got to temp
    ordering = ['-date_posted']  # newest to oldest
    # ordering = ['date_posted'] oldest to newest

    # if you forgot it then is show error like
    # <app>/<models>_<viewtype>.html


class PostDetailView(DetailView):
    model = Post
