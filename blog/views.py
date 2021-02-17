from django.shortcuts import render

posts = [
    {
        'author': 'azhar',
        'title': 'Blog Post1',
        'content': 'firs post content',
        'date_posted': "august 27 2018"
    },
    {
        'author': 'Valar',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': "may 01 2018"
    },
    {
        'author': 'SilugGromRalab',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': "jan 14 2017"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':"About Author"})
