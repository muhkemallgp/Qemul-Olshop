from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from django.core import serializers
from main.models import Item
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse


# Create your views here.
def show_main (request):
    items = Item.objects.all()
    jumlah_barang = Item.objects.aggregate(total = Sum("amount"))['total']
    jumlah_item = Item.objects.count()

    if jumlah_barang == None:
        jumlah_barang = 0

    context = {
        "Nama_Aplikasi" : "main",
        "Nama" : "Muh. Kemal Lathif Galih Putra",
        "Kelas" : "PBP - D",
        "items"  : items,
        "jumlah_jenis" : jumlah_item,
        "jumlah_barang" : jumlah_barang
    }
    return render(request,"homepage.html",context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")