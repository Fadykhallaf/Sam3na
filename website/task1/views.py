from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from django.shortcuts import render, redirect
from .forms import LoginUserForm, UserRegisterForm


def login_view(request):
    print(request.user.is_authenticated())
    title = 'Sing In'
    form = LoginUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        redirect("music:index")
        print(request.user.is_authenticated())

    return render(request, 'form1.html', {'form': form, 'title': title})


def register_view(request):
    title = 'Register'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        redirect("/")

    context = {
        'form':form,
        'title':title
    }
    return render(request, 'form1.html', context)


def logout_view(request):
    logout(request)
    redirect("/")