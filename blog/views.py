from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    """this is public home post"""
    # this is class based view djang0 support few of them like ListView , DetailView, delete update etc
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'  # what variable posts ll got to temp
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 2
    # ordering = ['date_posted'] oldest to newest

    # if you forgot it then is show error like
    # <app>/<models>_<viewtype>.html


class UserPostListView(ListView):
    """this is user post only """
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    """inbuild in django help to assign author as a login user  when creating a new post"""

    def form_valid(self, form):
        # inbuilt function in CreateView
        form.instance.author = self.request.user
        # take that instance and set to author
        return super().form_valid(form)
        # running form_valide method on parent class


"""you cant use decorator on class that y we used login req mixin"""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

    """test_func which is inbuild give a test is user which is logged in is same as author of the post when updating"""

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    # form_valid >> when user is login and its create a post then it ll assign author as user which is logged in
