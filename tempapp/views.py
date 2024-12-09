from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url='/signin')
def home(request):
    posts = Post.objects.all()
    a = {
        'posts': posts,
    }
    return render(request, 'index.html' , context=a)

def account_settings(request):
    return render(request, 'account-setting.html')

def profile(request):
    return render(request, 'profile.html')


def settings(request):

    return render(request, 'setting.html')




def signin(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        auth = authenticate(request, username=username, password=password)

        if auth:
            login(request, auth)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('/')

        return render(request, 'signin.html', context={'error': 'username or password  incorrect'})

    return render(request, 'signin.html')




@login_required(login_url='/signin')
def logout_view(request):
    logout(request)
    return redirect('/')




def signup(request):
    if request.user.is_authenticated:
        return redirect('/')


    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        exists = User.objects.filter(username=username).first()
        if exists:
            return render(request, 'signup.html', context={'error': 'username has already been taken'})
        user = User.objects.create(username=username, password=make_password(password))
        user.save()
        return redirect('/signin')

    return render(request, 'signup.html')