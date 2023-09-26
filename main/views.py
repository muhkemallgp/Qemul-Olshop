from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime


# Create your views here.
@login_required(login_url='/login')
def show_main (request):
    items = Item.objects.filter(user = request.user)
    jumlah_barang = Item.objects.filter(user = request.user).aggregate(total = Sum("amount"))['total']
    jumlah_item = Item.objects.filter(user = request.user).count()

    if jumlah_barang == None:
        jumlah_barang = 0

    context = {
        "Kata_Awal" : "Ayo Beli Yuk!",
        "Nama" : request.user.username,
        "Kelas" : "PBP - D",
        "items"  : items,
        "jumlah_jenis" : jumlah_item,
        "jumlah_barang" : jumlah_barang,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request,"homepage.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request,id):
    jumlah = Item.objects.get(pk =id)
    jumlah.amount+=1
    jumlah.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def sub_amount(request,id):
    jumlah = Item.objects.get(pk=id)
    jumlah.amount-=1
    if jumlah.amount == 0:
        jumlah.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    jumlah.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_amount(request,id):
    jumlah = Item.objects.get(pk=id)
    jumlah.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
    

@login_required(login_url='/login')
def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")