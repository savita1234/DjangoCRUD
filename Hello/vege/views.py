from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/receipe/login")
def receipe(request):
    if request.method == "POST":
        data = request.POST
        r_name = data.get('r_name')
        r_detail = data.get('r_detail')
        file = request.FILES.get('r_file')
        Receipe.objects.create(
            receipe_name = r_name,
            receipe_description = r_detail,
            receipe_image = file,
            user = request.user
        )
        return redirect('/receipe/details')
    return render(request, 'vege/index.html')
    #return HttpResponse("hello this is receipe page")

@login_required(login_url="/receipe/login")
def name(request):
    receipes = Receipe.objects.filter(user=request.user)
    context = {'receipes': receipes}
    return render(request, 'vege/detail.html',context)
    
@login_required(login_url="/receipe/login")
def delete_receipe(request, id):
    delete_receipe = Receipe.objects.get(id = id)
    delete_receipe.delete()
    return redirect('/receipe/details')
    # return HttpResponse(id)

@login_required(login_url="/receipe/login")
def update_receipe(request, id):
    receipe = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        name = data.get('r_name')
        description = data.get('r_detail')
        image = request.FILES.get('r_file')

        receipe.receipe_name = name
        receipe.receipe_description = description
        if image:
            receipe.receipe_image = image
        receipe.save()
        return redirect('/receipe/details')

    context = {'receipe': receipe}
    return render(request, 'vege/update.html', context)


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username = email).exists():
            return HttpResponse("invalid email")
            return redirect('/receipe/login')

        user = authenticate(username = email, password = password)
        if user is None:
            return HttpResponse("invalid password")
            return redirect('/receipe/login')

        else:
            login(request, user)
            return redirect('/receipe/details')


    return render(request, 'vege/login.html')

@login_required(login_url="/receipe/login")
def user_logout(request):
    logout(request)
    return redirect('/receipe/login')


def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = email)
        if user.exists():
            return redirect('/receipe/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = email,
        )
        user.set_password(password)
        user.save()
        return redirect('/receipe/login')

    return render(request, 'vege/register.html')