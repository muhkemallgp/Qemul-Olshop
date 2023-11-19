import json
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from main.models import Item
from main.forms import  RegisterForm, ItemForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import datetime


@csrf_exempt
def create_item_flutter_new(request):
    if request.method == 'POST':
        # print("TEST 1")
        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = 1,
            description = data["description"]
        )
        print("TEST 2")
        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
# Create your views here.
@login_required(login_url='/login')
def show_main (request):
    jumlah_item = Item.objects.filter(user = request.user).count()
    if(jumlah_item != 0):
        items = Item.objects.filter(user = request.user)[:jumlah_item-1]
    else:
        items = Item.objects.filter(user = request.user)
    
    item_akhir = Item.objects.filter(user = request.user).last()
    jumlah_barang = Item.objects.filter(user = request.user).aggregate(total = Sum("amount"))['total']

    if jumlah_barang == None:
        jumlah_barang = 0

    context = {
        "Kata_Awal" : "Ayo Beli Yuk!",
        "Nama" : request.user.username,
        "Kelas" : "PBP - D",
        "items"  : items,
        "item_akhir": item_akhir,
        "jumlah_jenis" : jumlah_item,
        "jumlah_barang" : jumlah_barang,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request,"homepage.html",context)

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
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

def get_items_json(request):
    items = Item.objects.filter(user = request.user)
    if(items != None):
        return HttpResponse(serializers.serialize('json', items))
    return HttpResponse(0)

def get_all_amount(request):
    jumlah_barang = Item.objects.filter(user = request.user).aggregate(total = Sum("amount"))['total']
    return HttpResponse(jumlah_barang)

@csrf_exempt
def add_items_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

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

@csrf_exempt
def delete_items_ajax(request,id):
    if request.method == 'DELETE':
        jumlah = Item.objects.get(pk=id)
        jumlah.delete()
        return HttpResponse(b"DELETE", status=201)
    
    return HttpResponseNotFound()

# def edit_product(request, id):
#     # Get product berdasarkan ID
#     product = Item.objects.get(pk = id)

#     # Set product sebagai instance dari form
#     form = ItemForm(request.POST or None, instance=product)

#     if form.is_valid() and request.method == "POST":
#         # Simpan form dan kembali ke halaman awal
#         form.save()
#         return HttpResponseRedirect(reverse('main:show_main'))

#     context = {'form': form,
#                "Nama" : request.user.username,
#                 "heading": "Edit Item!",
#                 "value_button":"Edit Item",
#                 "Kelas" : "PBP - D",}
#     return render(request, "edit_product.html", context)
    

@login_required(login_url='/login')
def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = { 'form': form,
                "Nama" : request.user.username,
                "heading": "Add Item!",
                "value_button":"Add Item",
                "Kelas" : "PBP - D",}
    return render(request, "add_item.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# @login_required(login_url='/login')
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