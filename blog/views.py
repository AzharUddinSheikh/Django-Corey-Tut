from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # inbuilt function in CreateView
        form.instance.author = self.request.user
        # take that instance and set to author
        return super().form_valid(form)
        # running form_valide method on parent class

    # form_valid >> when user is login and its create a post then it ll assign author as user which is logged in
