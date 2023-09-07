from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
from django.contrib.auth import get_user_model

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def profile(request, username):
    User = get_user_model()
    user_info = User.objects.get(username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/profile.html', context)



def follow(request, username):
    
    User = get_user_model() 

    me = request.user
    you = User.objects.get(username=username) 

    if you in me.followings.all() :
        me.followings.remove(you)
    else:
        me.followings.add(you)

    return redirect('accounts:profile', username=username)

def logout(request):
    auth_logout(request)

    return redirect('accounts:login')
    
    
def followers(request, username):
    User = get_user_model()

    person = User.objects.get(username=username)

    context = {
        'person': person,
    }
    return render(request,'accounts/followers.html', context)

    for follower in followers_list:
        a = User.objects.get(username=follower.username)
        followers_name.append(a)


def followings(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)

    context = {
        'person': person,
    }
    return render(request,'accounts/followings.html', context)

def like_posts(request, username):
    User = get_user_model()
    user_info = User.objects.get(username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/like_profile.html', context)