from django.shortcuts import render

# Create your views here.
def home (request):
    context = {
        "Nama_Aplikasi" : "main",
        "Nama" : "Muh. Kemal Lathif Galih Putra",
        "Kelas" : "PBP - D"
    }
    return render(request,"homepage.html",context)
