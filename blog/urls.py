from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]


# we cant pass class like this PostListView to convert it into actual view we need this method as_view


'''
detailclass view 
lets say we need to create a route to take us to a specific post 
ex = let  say we want to see post for blog one that url something like post/1 
so if you want to create a route where the id of a post is acutally part of the route
then we can create a route 
'''
