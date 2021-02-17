from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account Created for {username} Now Login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

# request.POST = request.POST is a data when we Request is POST and form ll created
# replace UserCreationForm >> UserRegisterForm (bvoz its already a child class of that)
