## A. Aplikasi Online Shopping 
[QEMUL OLSHOP](https://qemulolshop.adaptable.app/main/)

## B. Tata Cara Implementasi Checklist

### 1. Membuat sebuah project Django Baru

#### a) Membuat direktori baru sesuai nama proyek (inventory) yang dinginkan `qemul_olsop`.

#### b) Membuat berkas Dependencies dengan nama `requirements.txt` untuk deployment proyek. Lalu disimpan di dalam direktor proyek.

Isi file `requirements.txt`:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

#### c) Membuat virtual environment untuk proyek.
```
python -m venv venv
```

#### d) Mengaktivasi virtual environment.
```
env\Scripts\activate.bat
```

#### e) Menginstal library keperluan proyek dengan cara:
```
pip install -r requirements.txt
```

#### f) Lalu buat proyek Django baru dengan nama `olshop_project`,
```
django-admin startproject olshop_project .
```

**Keterangan :** Langkah **c - f** diatas dilakukan didalam cmd terminal yang sudah berada di direktori `qemul_olsop`.

### 2. Membuat aplikasi dengan nama `main` pada proyek tersebut.

Sebelum membuat aplikasi `main`, pastikan langkah 1 diatas sudah dilaksanakan semua.

#### a) Membuka cmd terminal di direktori `qemul_olsop`. Lalu jalankan perintah:
```
python manage.py startapp main
```

#### b) Menambahkan aplikasi `main` kedalam proyek:

- Buka `settings.py` yang berada didalam proyek `olshop_project`.

- Cari variabel `INSTALLED_APPS`.

- Tambahkan kata `main` sebagai nama aplikasi kita kedalam variable tersebut.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

### 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.

Pastikan langkah 1 dan 2 diatas sudah dilakukan.

#### Hubungkan routing URL proyek **`olshop_project`** dengan  aplikasi `main` :

- Buka file `urls.py` yang berada didalam direktori proyek **`olshop_project`** 

- Tambahkan kode sebagai berikut :
```python
...
from django.urls import path, include
...

urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
Kode diatas berarti jika dari URL website utama kita lalu ketemu *path* `main/` maka dari `url.py` proyek akan routing ke `url.py` yang berada di aplikasi `main`.

### 4. Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib yang ditentukan.

Pastikan langkah-langkah diatas sudah dilakukan.

#### a) Membuka file `models.py` yang berada di direktori aplikasi `main`.

#### b) Tambahkan kode sebagai berikut :
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
Kode diatas berarti proyek kita sudah memiliki class model yang bisa mendapatkan data dari website lalu ditransfer ke database.
#### Note: 
Setiap perubahan di `models.py` harus selalu di migration kan.

### 5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Pastikan langkah diatas sudah dilakukan semua.

#### a) Buatlah direktori baru bernama `template` di direktori `main`. Lalu buatlah didalam direktori template, file bernama `homepage.html` yang merupakan file *HTML* yang dapat divisualisasikan ke dalam proyek website kita.

Isi kode `homepage.html` :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QEMUL OLSHOPt</title>
</head>
<body>
    <h1>Welcome to Qemul Olshop</h1>
    <h4>Nama Aplikasi: {{Nama_Aplikasi}}</h4>
    <h4>Nama: {{Nama}}</h4>
    <h4>Kelas: {{Kelas}}</h4>
</body>
</html>
```
Kode diatas mengimplementasikan konsep template variabel, yaitu konten dari html ( contoh : {{Nama}} ) ini tidak langsung ditulis diberkas template, tetapi di passing dari `views.py`.

#### b) Membuat file `views.py` di dalam direktori aplikasi `main`. Lalu isi dengan kode berikut:
```python
from django.shortcuts import render

# Create your views here.
def home (request):
    context = {
        "Nama_Aplikasi" : "main",
        "Nama" : "Muh. Kemal Lathif Galih Putra",
        "Kelas" : "PBP - D"
    }
    return render(request,"homepage.html",context)

```
Dengan kode diatas kita membuat suatu fungsi yang menerima input *request* dari `urls.py` aplikasi, lalu kita return fungsi render yang berguna untuk menampilkan `homepage.html` dengan variabel tambahan `context` yang akan *dipassing* di dalam file *HTML*-nya.


### 6. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.

#### a) Membuat file `urls.py` di dalam direktori `main`.

#### b) Isi file `urls.py` dengan kode berikut :
```python
from django.urls import path
from main.views import home

urlpatterns = [
    path("", home)
]
```

Langkah ini dilakukan agar rute URL di dalam aplikasi `main` dapat diakses. 
Contoh:
- main/ 
- main/lorep (Belum bisa diakses)
- main/ipsum (Belum bisa diakses)

Kita dapat menghubungkan `urls.py` di aplikasi `main` dengan `views.py` melalui `home` yang merupakan fungsi dari `views.py`. 

Ini berarti setiap ada path `main/` dari website proyek, maka dari `urls.py` di `olshop_project` akan masuk ke `urls.py` di `main`. Lalu akan memanggil fungsi `home` dari `views.py`.

### 7.Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

#### a) Membuka website [adaptable.io](https://adaptable.io/)

#### b) Sign-up dengan akun Github kita.

#### c) Pilih opsi _deploy a new app_. 

#### d) Pilih repositori `Qemul_Olshop` yang berisi direktori `qemul_olsop` yang sudah dipush ke github.
 
#### e) Pilih _Python App Template_ sebagai _template deployment_. 

#### f) Pilih PostgreSQL sebagai pilihan database. 

#### g) Masukkan python dengan versi lokal (3.11) lalu masukan prompt `python manage.py migrate && gunicorn olshop_project.wsgi` pada _Start Command_. 

#### h) Tentukan nama aplikasi: [qemulolshop](https://qemulolshop.adaptable.app/main/) 

#### i) Checklist _HTTP Listener on PORT_.

## C. Bagan Request Dari Client - Django - Respon
<img src = dokumen_tambahan\Bagan_Django.png>

#### Penjelasan:
Django flow dimulai dari client/user yang mencari url *path* di bar pencarian, lalu dari link url akan diberikan ke `urls.py`. Disini `urls.py` akan men assign link urls yang bersangkutan dengan fungsi yang sudah ditentukan di dalam `views.py`. 

Lalu dari fungsi yang ada di `views.py` akan diolah terlebih dahulu melalui model yang sudah dibuat sebelumnya di `models.py`, khususnya jika terdapat data input atau output dalam flow ini. Lalu `models.py` akan mentrasaksikan data ke database yang bisa dipanggil lagi dari model ke `views.py`.

Dari `views.py` yang sudah mendapatkan data dari database melalui `models.py` maka akan menulis data tersebut ke template *HTML* yang telah dibuat sesuai permintaan yang dimana hasil akhir *HTML* ini akan ditampilkam ke layar client/user.

## D. Virtual Environment

Virtual environment penting untuk mengisolasi dependensi dalam proyek Python, khususnya Django agar pip/library/version yang digunakan antar proyek yang satu dengan yang lain tidak saling beririsan dan membuat konflik. 

Meskipun bisa membuat Django tanpa itu, tetapi berisiko error jika terdapat collapse (tumpang tindih) antar proyek. Oleh karena itu, virtual environment yang dapat mengisolasi dependensi dan memastikan proyek hanya menginstal paket yang diperlukan dapat memudahkan pengguna lain dan disarankan dalam pengembangan Django.

## E. MVC, MVT, dan MVVM
Setiap konsep arsitektur memiliki cara tersendiri untuk mengatur komponen aplikasi, memudahkan pengembangan dan pemeliharaan. Pemilihan tergantung pada jenis aplikasi, teknologi, dan preferensi pengembang.

1. **MVC (Model-View-Controller)**:
   - **Model**: Bertanggung jawab untuk mengelola data dan logika bisnis aplikasi.
   - **View**: Menampilkan informasi dari model kepada pengguna dan mengumpulkan input dari mereka.
   - **Controller**: Menerima input dari pengguna, memprosesnya, dan mengirimkan perintah ke model atau view yang sesuai.

   **Perbedaan**: MVC adalah arsitektur yang digunakan dalam pengembangan perangkat lunak secara umum, tidak hanya pada web. Model mengelola logika bisnis, View menangani tampilan, dan Controller mengontrol aliran data antara keduanya.

2. **MVT (Model-View-Template)**:
   - **Model**: Serupa dengan MVC, mengelola data dan logika bisnis.
   - **View**: Menampilkan data dari model, tetapi dalam Django, ini juga mengendalikan logika presentasi.
   - **Template**: Bertanggung jawab untuk merender tampilan secara dinamis dengan memasukkan data dari model.

   **Perbedaan**: MVT adalah variasi dari MVC yang digunakan dalam Django, sebuah kerangka kerja web Python. Dalam MVT, peran View lebih kompleks karena juga mencakup sebagian dari logika presentasi yang dipecah menjadi Template.

3. **MVVM (Model-View-ViewModel)**:
   - **Model**: Sama dengan MVC dan MVT, mengelola data dan logika bisnis.
   - **View**: Menampilkan data dari ViewModel.
   - **ViewModel**: Berfungsi sebagai penghubung antara Model dan View. Ini mengubah data dari Model ke format yang dapat ditampilkan oleh View dan menangani banyak aspek logika tampilan.

   **Perbedaan**: MVVM adalah arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang lebih kompleks, seperti aplikasi desktop atau aplikasi berbasis seluler. Ini memisahkan lebih banyak logika tampilan ke ViewModel, yang membantu dalam pengujian dan pemisahan tugas.

Perbedaan utama antara ketiganya adalah dalam cara mereka mengatur dan memisahkan tanggung jawab antara komponen Model, View, dan Controller/Template/ViewModel. MVC adalah konsep generik yang digunakan dalam berbagai konteks, sementara MVT adalah spesifik untuk Django dalam pengembangan web, dan MVVM lebih umum digunakan dalam pengembangan aplikasi dengan antarmuka pengguna yang lebih kompleks.


