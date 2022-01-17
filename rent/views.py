from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rent.form import *
from rent.models import *
from rent.filters import HouseDetailFilter


# Create your views here.


def index(request):
    houses = HouseDetail.objects.all()
    clientchecks = ClientCheck.objects.all()
    myFilter = HouseDetailFilter()
    dic = {
        'houses': houses,
        'clientchecks': clientchecks,
        'myFilter': myFilter
    }
    print(houses)
    return render(request, 'rent/index.html', dic)


def log(request):
    return render(request, 'rent/login.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('log')
            except:
                pass
    else:
        form = RegisterForm()

    return render(request, 'rent/signup.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print('hello')
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('signup')
    else:
        return redirect('log')


def add_post(request):
    clientchecks = ClientCheck.objects.all()
    return render(request, 'users/add_post.html', {'clientchecks': clientchecks})


def add_post_views(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                pass
    else:
        form = AddPostForm()
        return render(request, 'rent/index.html', {'form': form})


def logout_views(request):
    logout(request)
    return redirect('index')


def success(request):
    return HttpResponse('successfully uploaded')


def details(request, id):
    house = HouseDetail.objects.filter(id=id)
    print(id)
    return render(request, 'users/details.html', {'house': house})


def profile(request, id):
    houses = HouseDetail.objects.filter(user=id)
    clientchecks = ClientCheck.objects.all()
    dic = {
        'houses': houses,
        'clientchecks': clientchecks
    }
    return render(request, 'users/profile.html', dic)


def search_rent(request):
    if request.method == "POST":
        loc = request.POST['search_location']
        if loc == '':
            print(0)
            ren = request.POST['search_rent_type']
            sch = HouseDetail.objects.filter(rent_type__icontains=ren)
            return render(request, 'rent/search_result.html', {'sch': sch})
        print(1)
        form = SearchRentForm(request.POST)
        if form.is_valid():
            print(2)
            key = form.cleaned_data['search_location']
            print(key)
            v = form.cleaned_data['search_rent_type']
            print(v)
            if v == 'any':
                sch = HouseDetail.objects.filter(location__icontains=key)

            else:
                sch = HouseDetail.objects.filter(location__icontains=key, rent_type__icontains=v)
                # clientchecks = ClientCheck.objects.all()
            dic = {
                'sch': sch,
                # 'clientchecks': clientchecks
            }
            return render(request, 'rent/search_result.html', dic)
    return redirect('index')


def delete_views(request, id):
    ob = HouseDetail.objects.filter(id=id)
    ob.delete()
    return redirect('index')
