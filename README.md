# TUGAS 5 PBP
## A. Element Selector
#### Element Selector (tag)
Selector ini memungkinkan kita untuk memilih elemen HTML berdasarkan tipe tag. Ini adalah selektor yang paling umum digunakan dan bisa digunakan dalam hampir semua kasus. Misalnya, jika kita ingin mengganti gaya semua elemen p pada halaman, kita bisa menggunakan selector p. 

Waktu yang tepat untuk menggunakannya adalah saat kita ingin mengganti gaya pada seluruh elemen dengan tipe tag yang sama.

#### Class Selector (.class)
Class selector memungkinkan kita untuk memilih elemen berdasarkan nilai atribut class. Ini berguna saat kita ingin mengganti gaya beberapa elemen yang memiliki kelas yang sama, tetapi tidak semua elemen dengan tipe tag yang sama harus diubah gayanya. Class selector sangat fleksibel dan sering digunakan dalam pengembangan web.

#### ID Selector (#id)
ID selector memungkinkan kita untuk memilih elemen berdasarkan nilai atribut id. ID seharusnya unik dalam halaman, jadi kita biasanya menggunakannya untuk mengidentifikasi elemen tertentu. Ini cocok digunakan ketika kita ingin mengganti gaya satu elemen tertentu.

#### Attribute Selector ([attribute])
Attribute selector memungkinkan kita untuk memilih elemen berdasarkan atribut mereka. kita bisa memilih elemen yang memiliki atribut tertentu, misalnya, 
```html
<a href="...">
``` 
dengan [href] selector. kita juga bisa menggunakan selector ini dengan nilai atribut tertentu, misalnya, [href="https://example.com"].

## B. HTML5 
HTML adalah bahasa markup yang digunakan untuk membuat halaman web. HTML5 adalah versi terbaru dari HTML yang menghadirkan sejumlah perbaikan dan fitur baru, seperti dukungan untuk video dan audio langsung, grafik vektor, dan penyimpanan lokal. 

Kelebihan HTML5 meliputi peningkatan kinerja, kompatibilitas lintas peramban yang lebih baik, dan kemampuan untuk mengembangkan aplikasi web yang lebih interaktif dan canggih tanpa perlu plugin tambahan seperti Flash. Hal ini membuat HTML5 menjadi pilihan utama dalam pengembangan web modern.

Beberapa tag HTML5 yang umum digunakan adalah:

- `<header>`: Digunakan untuk bagian atas halaman web, biasanya berisi judul atau logo.

- `<nav>`: Digunakan untuk menampilkan menu navigasi.

- `<section>`: Digunakan untuk membagi konten dalam sebuah halaman.

- `<article>`: Digunakan untuk mempresentasikan konten independen yang dapat berdiri sendiri.

- `<aside>`: Digunakan untuk konten yang terkait dengan konten lain, seperti sidebar.

- `<footer>`: Digunakan untuk bagian bawah halaman, seringkali berisi informasi kontak atau hak cipta.

- `<figure>`: Digunakan untuk menyertakan media seperti gambar atau grafik, sering digunakan dengan `<figcaption>`.

## C. Margin dan Padding
#### Margin
Margin adalah jarak antara batas elemen dengan elemen lain di sekitarnya. Margin tidak memiliki background atau warna, dan biasanya digunakan untuk mengatur jarak antara elemen-elemen. Margin akan memengaruhi elemen secara eksternal.

#### Padding
Padding adalah jarak antara batas elemen dengan kontennya sendiri. Padding akan memengaruhi elemen secara internal, yaitu jarak antara batas elemen dan kontennya. Padding digunakan untuk mengatur ruang di dalam elemen.

Contoh Implementasi:

![Alt text](/dokumen_tambahan/Tugas%205/image.png)

## D. CSS _Tailwind_ dan _Bootstrap_
#### Tailwind CSS
Tailwind adalah framework CSS yang memungkinkan kita untuk merancang tampilan web dengan memanfaatkan kelas-kelas utilitas yang telah ditentukan. Ini memberikan kontrol yang sangat detail dan fleksibilitas dalam mengatur tampilan. Tailwind cocok digunakan ketika kita ingin merancang tampilan yang sangat kustom dan memiliki pemahaman yang baik tentang CSS.

#### Bootstrap
Bootstrap adalah framework CSS yang menyediakan komponen dan kelas yang telah siap digunakan untuk merancang tampilan web yang responsif. Ini adalah solusi cepat untuk membangun tampilan yang konsisten dan bersih tanpa banyak kustomisasi CSS. Bootstrap cocok digunakan saat kita ingin membuat prototipe cepat atau membangun situs web tanpa harus menulis banyak kode CSS dari awal.

Jika kita ingin cepat membangun tampilan responsif dengan sedikit usaha kustomisasi, Bootstrap bisa menjadi pilihan yang baik. 

Jika kita ingin tampilan yang sangat kustom dan lebih mendalam dalam pemahaman CSS, Tailwind bisa lebih sesuai.


## E. Implementasi Checklist
### 1. Kustomisasi halaman `login`, `register`, dan `add_item` semenarik mungkin.
Sebelum kustomisasi `login`, `register`, dan `add_item` saya mencopy link dan script bootstrap dari websitenya ke `base.html` agar dapat terdeteksi atribut dari bootstrapnya.

Saya juga meload static karena di navbar saya ada menggunakan gambar static.

#### a) Halaman `login`:
1. Membuat navbar template di `base.html` agar tidak usah melakukannya disetiap page.
2. Membuat beberapa _div_ sesuai konten sehingga tampilan login saya berada ditengah page.
3. Merubah class button saya menjadi `btn-primary`.
4. Menambahkan `footer` sebagai penanda bahwa ini adalah website `qemulshop`.

Tampilan `login`:
![Alt text](/dokumen_tambahan/Tugas%205/image-1.png)

#### b) Halaman `register`:
1.  Membuat _div_ sebagai keseluruhan page dahulu.
2. Membuat class baru di `forms.py` di  main untuk menambahkan setiap atribut yang dimiliki oleh model `UserCreationForm`. Untuk menyesuaikan styling.
```py
...
 def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'input-field', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Username', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
...
```
Dengan kode diatas kita menupdate atribute dan syarat dari username dapat dibentuk.

3. Memasukkan icon-icon dari `fa-fa` website dengan mengarahkannya berada di area inputan. 
4. Memberikan styling secaran internal dan inline untuk membuat tampilan menjadi lebih sesuai.

Tampilan `register`:
![Alt text](/dokumen_tambahan/Tugas%205/image-2.png)

#### c) Halaman `add_item` atau tambah inventori.
1. Menambahkan navbar yang sudah di ada dari `homepage`, tetapi di ubah untuk menyesuaikan.
2. Menambahkan update atribut untuk ItemForm seperti:
```py
...
def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['name'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'name', 
            'id':'name', 
            'type':'text', 
            'placeholder':'Nama Barang', 
            })
...
```

Dengan kode diatas kita juga menupdate atribut dari masing-masing fields yang ada di model Item agar sesuai dengan styling yang ingin kita jalankan.

Tampilan `add_item`:
![Alt text](/dokumen_tambahan/Tugas%205/image-3.png)

3. Merubah layout _forms_ yang awalnya menggunakan table menjadi _div_ dan mengubah class dari _div_-nya.

### 2. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
1. Mengedit navbar agar ada nama website, user, add_item, dan logout.
2. Membuat invetori menjadi sebuah card. Dalam hal ini saya memanfaatkan loop for design card yang sama.
3. Menambahkan fungsi, file html, dan button edit inventori yang dipelajari tutorial sebelumnya.
4. Menambahkan last sesi login menjadi footer.
5. Lalu diakhir merubah sedikit design index objek terakhir (Untuk Bonus Poin).

Tampilan `homepage`:
![Alt text](/dokumen_tambahan/Tugas%205/image-4.png)

<br>

# TUGAS 4 PBP
<hr>

## A. Django `UserCreationForm`
Django `UserCreationForm` adalah sebuah bentuk (form) bawaan dalam kerangka kerja Django yang digunakan untuk membuat formulir pendaftaran pengguna (user registration form). Form ini dirancang khusus untuk membuat pengguna baru dengan informasi seperti username, password, dan konfirmasi password. 

`UserCreationForm` telah terintegrasi dengan sistem otentikasi Django, sehingga memudahkan pengembang untuk mengimplementasikan fitur pendaftaran pengguna dalam aplikasi web Django mereka. 

Kelebihan dari `UserCreationForm` meliputi:

#### 1) Kemudahan Penggunaan: Form ini sudah terintegrasi dengan Django, sehingga mudah digunakan tanpa perlu menulis kode form dari awal.
#### 2) Validasi Bawaan: Form ini melakukan validasi otomatis terhadap data yang dimasukkan oleh pengguna, seperti memastikan bahwa password yang dimasukkan cocok.

Beberapa kekurangan `UserCreationForm` meliputi:

#### Tampilan Default: Form ini memiliki tampilan default yang sederhana, jadi jika kita ingin menyesuaikan tampilan sesuai dengan kebutuhan aplikasi kita, kita perlu menambahkan kode tambahan.

## B. Autentikasi dan Otorisasi
__Autentikasi__ dan __otorisasi__ adalah dua konsep penting dalam pengembangan web, termasuk dalam konteks Django:

- __Autentikasi__ adalah proses verifikasi identitas pengguna. Dalam Django, ini berarti memeriksa apakah pengguna memiliki kredensial yang valid (biasanya username dan password) untuk mengakses sistem.

- __Otorisasi__ adalah proses pengendalian akses terhadap sumber daya atau tindakan tertentu dalam sistem. Setelah pengguna terautentikasi, otorisasi menentukan apakah pengguna tersebut memiliki izin untuk melakukan tindakan atau mengakses sumber daya tertentu.

Keduanya penting karena autentikasi menjaga keamanan sistem dengan memastikan bahwa hanya pengguna yang sah yang dapat mengaksesnya, sementara otorisasi memastikan bahwa pengguna hanya memiliki akses ke bagian sistem yang sesuai dengan izin mereka.

## C. _Cookies_ dalam aplikasi website
_Cookies_ dalam konteks aplikasi web adalah sepotong data yang disimpan di sisi klien (biasanya dalam browser pengguna) dan digunakan untuk menyimpan informasi sesi atau preferensi pengguna. Django menggunakan _cookies_ untuk mengelola data sesi pengguna dengan cara yang aman. Ini membantu mengidentifikasi pengguna dan menyimpan informasi seperti ID sesi, preferensi, atau status login.

## D. Resiko penggunaan _Cookies_
Penggunaan cookies secara default dalam pengembangan web bisa dibilang relatif aman, terutama jika digunakan dengan benar. 

Namun, ada beberapa risiko potensial yang harus diwaspadai:

#### 1) Pelacakan
Cookies dapat digunakan untuk melacak aktivitas pengguna secara online, yang bisa menganggu privasi pengguna. Beberapa perusahaan atau entitas dapat menggunakan cookies untuk mengumpulkan data pengguna tanpa izin mereka.

#### 2) Kekuatan Kata Sandi
Jika cookies digunakan untuk menyimpan token otentikasi atau informasi sensitif lainnya, peretas yang berhasil mencurinya dapat memanfaatkannya untuk mengakses akun pengguna. Oleh karena itu, penting untuk melindungi cookies dengan enkripsi dan mekanisme keamanan yang kuat.

#### 3) Cookie Theft (Pencurian Cookie)
Peretas dapat mencuri cookies dari perangkat pengguna melalui serangan seperti cross-site scripting (XSS) atau man-in-the-middle (MITM) attack.

Penting untuk mengimplementasikan cookies dengan bijak dan mempertimbangkan keamanan serta privasi pengguna dalam pengembangan aplikasi web kita. Selain itu, kita dapat menggunakan teknik seperti enkripsi dan HTTPS untuk meningkatkan keamanan cookies dan data yang disimpan di dalamnya.

## E. Tatacara Implementasi
### 1. Mengimplementasikan fungsi registrasi, login, dan logout ditambah dengan menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

#### a) Menjalankan virual environment seperti di tutorial

#### b) Membuat fungsi baru `register` yang menerima input request dalam file `views.py` di `main`

#### c) Menambahkan import `redirect`, `UserCreationForm`, dan `messages` diatas dengan kode berikut:
```py
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

#### d) Menambahkan kode fungsi `register`, `login_user`, dan `logout_user` seperti berikut:
Fungsi Register:
```py
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
```
Dengan menambahkan kode berikut kedalam fungsi register kita dapat membuat user baru dengan bantuan templates `UserCreationForm` dari Django.

Fungsi login_user:
```py
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
```
Dengan kode diatas kita membuat fungsi yang bisa membuat `user` yang sudah `register` untuk `login` ke website kita dan mengakses website sesuai dengan data dari masing-masing `user`.

Fungsi logout_user:
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Dengan kode diatas  kita dapat `logout` dari tampilan website dan mengakhiri `cookiesnya`.

#### e) Membuat file `regiter.html` dan `login.html` didalam folder `templates` dalam `main` dengan kode:
FIle `register.html`:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
Dengan kode diatas kita dapat menampilkan tampilan untuk mendaftarkan user baru di website kita.

File `login.html`:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login To QemulShop</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
Dengan kode diatas, `user` yang telah `register` dapat `login` di tampilan website kita.

#### f) Menambahkan fungsi `register`, `login_user`, dan `logout_user` ke `urls.py` di `main` kita dengan cara menambahkan kode berikut:
```py
from main.views import register, login_user, logout_user
```
```py
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```
Dengan kode diatas kita mengimport fungsi `register`,`login_user`, dan `logout_user` dari `views.py` ke `urls.py` dalam `main`.

### 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat.

#### a) Melakukan runserver pada komputer
```sh
python manage.py runserver
```
Dengan kode diatas kita membuat local host webisite buatan kita
#### b) Mendaftarkan user baru dengan klik `Register Now` di tampilan website login
__Tampilan login__
<br>
<img src = dokumen_tambahan\login.jpg>
<br>

#### c) Buatlah username dan password sesuai yang diinginkan tetapi sesuai aturan security lalu klik daftar.
__Tampilan Register__
<br>
<img src = dokumen_tambahan\register.jpg>
<br>

#### d) Login sesuai akun yang telah didaftarkan dan add item sesuai yang diinginkan. Maka hasil akhirnya akan seperti:
__User 1__
<br>
<img src = dokumen_tambahan\user1.jpg>
<br>

__User 2__
<br>
<img src = dokumen_tambahan\user2.jpg>
<br>

### 3. Menghubungkan model Item dengan User.
#### a) Menambahkan kode berikut kedalam `model.py` di `main`:
```py
from django.contrib.auth.models import User
```
```py
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Dengan kode diatas kita dapat membuat relasi antar `user` dengan `Item` melalui `ForeignKey` dengan many to one relasi.

#### b) Mengubah fungsi `add_item` seperti berikut:
```py
def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)
```
Dengan kode berikut kita dapat memasangkan `Item` dari `form` sesuai dengan `user` yang `login`.

#### c) Mengubah fungsi `show_main` seperti berikut:
```py
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
```
Dengan kode diatas `Item` dan info `user` nya akan tersimpan sesuai `user` yang `login`.

#### d) Lalu lakukan `makemigrations` dan `migrate` dan submit `1` dan `1` untuk setiap perintah yang diminta.
```sh
python manage.py makemigrations
python manage.py migrate
```
Dengan melakukan perubahan pada diatas maka kita sudah merubah `model.py` kita sesuai kode terbaru kita.

<br>

# TUGAS 3 PBP
<hr>

## A. Perbedaan form `POST` dan form `GET` dalam Django
Perbedaan utama antara form POST dan form GET dalam Django adalah cara data dikirimkan dari halaman web ke server:

1. Form `POST` (HTTP method: POST):
   - Data dikirimkan secara tersembunyi dalam body permintaan HTTP.
   - Cocok digunakan untuk mengirim data sensitif seperti kata sandi.
   - Tidak terbatas pada panjang data yang dapat dikirimkan.
   - Tidak tampil di URL, sehingga lebih aman dari sisi privasi.

Contoh penggunaan umum form POST dalam Django adalah ketika mengirimkan formulir pendaftaran pengguna atau mengirimkan data ke server untuk memproses.

```html
<form method="post" action="/submit/">
    <!-- Isi formulir -->
    <input type="submit" value="Submit">
</form>
```

2. Form `GET` (HTTP method: GET):
   - Data dikirimkan melalui URL dalam bentuk query string.
   - Tidak cocok untuk data sensitif karena terlihat dalam URL.
   - Terbatas pada panjang URL yang dapat digunakan (tergantung pada browser dan server).
   - Berguna untuk pencarian atau filter data karena parameter dapat dilihat dan dibagikan melalui URL.

Contoh penggunaan umum form GET dalam Django adalah ketika membuat tautan untuk menyaring atau mencari data:

```html
<form method="get" action="/search/">
    <!-- Isi formulir pencarian -->
    <input type="text" name="query">
    <input type="submit" value="Search">
</form>
```

Pilihan antara POST dan GET harus dipilih sesuai dengan kebutuhan aplikasi, dengan mempertimbangkan keamanan, privasi, dan fungsi yang diinginkan.

## B. Perbedaan XML, JSON, dan HTML dalam konteks pengiriman data
Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah sebagai berikut:

1. **XML (eXtensible Markup Language)**:
   - **Tujuan Utama**: XML dirancang untuk merepresentasikan dan mengirimkan data dalam bentuk struktur terstruktur yang dapat disesuaikan.
   - **Struktur**: XML menggunakan tag kustom untuk mendefinisikan struktur data. Ini memungkinkan pemodelan data yang kuat dan kompleks.
   - **Keuntungan**: Cocok untuk pertukaran data yang rumit antara sistem yang berbeda dan memiliki dukungan kuat untuk validasi data.
   - **Kekurangan**: Lebih berat dan kompleks dibandingkan dengan JSON dan HTML. Dibutuhkan lebih banyak overhead.

2. **JSON (JavaScript Object Notation)**:
   - **Tujuan Utama**: JSON digunakan untuk merepresentasikan data dalam format yang mudah dibaca dan dipahami oleh manusia dan mudah diproses oleh mesin.
   - **Struktur**: JSON menggunakan sintaksis objek dan larik untuk merepresentasikan data, menjadikannya lebih ringkas dan mudah digunakan.
   - **Keuntungan**: Ringan, mudah diproses oleh berbagai bahasa pemrograman, dan sering digunakan dalam API web.
   - **Kekurangan**: Tidak memiliki dukungan untuk metadata dan validasi data sekuat XML.

3. **HTML (HyperText Markup Language)**:
   - **Tujuan Utama**: HTML digunakan untuk mendefinisikan struktur dan tampilan konten web, bukan untuk pengiriman data mentah.
   - **Struktur**: HTML adalah bahasa markup yang digunakan untuk membuat halaman web yang dapat di-render oleh browser.
   - **Keuntungan**: Memungkinkan pembuatan tampilan web yang interaktif dan responsif, namun tidak efisien untuk pertukaran data mentah.
   - **Kekurangan**: Tidak dirancang untuk pengiriman data mentah, dan tidak sesuai untuk pertukaran data antara aplikasi.

Jadi, pilihan antara XML, JSON, atau HTML dalam pengiriman data akan sangat tergantung pada kebutuhan aplikasi. JSON umumnya digunakan untuk pertukaran data antara aplikasi dan dalam API web karena kejelasan dan keringkasan sintaksisnya. XML lebih sesuai jika kita memerlukan struktur data yang kompleks dan validasi yang ketat. HTML, di sisi lain, digunakan untuk membangun tampilan web.

## C. Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern.
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki sejumlah keunggulan yang sangat relevan dengan kebutuhan pengembangan aplikasi web saat ini:

1. **Keringkasan Sintaksis**: JSON menggunakan format yang ringkas dan mudah dipahami oleh manusia, sehingga memudahkan pembacaan dan debugging.

2. **Kemudahan Pengolahan**: JSON dapat dengan mudah diproses oleh berbagai bahasa pemrograman, termasuk JavaScript (yang umum digunakan di sisi klien), Python, Ruby, dan banyak lagi, berkat struktur data sederhana dalam bentuk objek dan larik.

3. **Efisien untuk Pengiriman**: JSON adalah format data ringan, sehingga mengurangi overhead saat mengirim data melalui jaringan. Hal ini membuatnya cocok untuk aplikasi web yang menekankan efisiensi dan kinerja.

4. **Dukungan untuk API REST**: Banyak aplikasi web modern berkomunikasi melalui API REST (Representational State Transfer), dan JSON menjadi format yang sangat umum digunakan dalam API REST. Ini memungkinkan aplikasi berbicara satu sama lain dengan cara yang konsisten dan mudah dimengerti.

5. **Kemampuan Serbaguna**: JSON mendukung struktur data yang serbaguna, termasuk objek bersarang dan larik, sehingga dapat digunakan untuk merepresentasikan berbagai jenis data, dari sederhana hingga kompleks.

6. **Integrasi dengan JavaScript**: JSON secara alami cocok dengan JavaScript, yang memungkinkan data JSON dapat diuraikan dengan mudah dan digunakan dalam kode JavaScript di sisi klien.

7. **Dukungan dalam Database**: Banyak database modern memiliki dukungan bawaan untuk penyimpanan dan pengambilan data dalam format JSON, yang mempermudah integrasi dengan aplikasi web.

8. **Dukungan Format Penuh**: JSON memiliki dukungan yang baik di berbagai alat, framework, dan pustaka yang digunakan dalam pengembangan aplikasi web modern.

Kesimpulannya, JSON adalah format data yang sangat fleksibel, mudah digunakan, dan efisien dalam pertukaran data antara aplikasi web modern. Karena kemudahan penggunaannya dan dukungannya yang luas, JSON telah menjadi standar de facto dalam komunikasi data di dunia web saat ini.

## D. Tata Cara Implementasi Checklist
Sebelum membuat form pastikan kita sudah punya base.html di template projek.
### 1. Membuat input form untuk menambahkan objek model pada app sebelumnya.

#### a) Membuat file baru pada folder `main` dengan nama `forms.py` dengan isi kode seperti berikut:
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

#### b) Menambahkan beberapa import di `views.py` yang ada di `main`.

```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```

#### c) Membuat fungsi baru di `views.py` di folder `main` dengan kode berikut:
```python
def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item", context)
```
Dengan kode diatas kita mengirim data yang sudah dalam objek `form Item`, jika form nya baru dibuat maka kita akan ke tampilan `homepage` awal dengan data form baru.

Jika belum ada form data maka kita akan membuat tampilan untuk mengadd Item baru.

#### d) Menambahkan fungsi `show_main` pada `views.py` di folder `main`.

```py
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
```

Dari kode diatas kita mengambil semua objek dalam `model Item` yang telah kita buat dalam bentuk `form`. Objek ini akan dipassing ke `show_main`.

Lalu juga ada kode untuk membuat Bonus poin (Berapa item dan Berapa jumlah).

#### d) Menambahkan import fungsi baru dari `views.py` ke `urls.py` di `main` dan membuat `path route` baru untuk tampilan `add Item` dengan kode berikut:
```py
from main.views import show_main, add_item
```
```py
path('add-item', add_item, name='add_item')
```
#### e) Membuat file `add_item.html` baru dalam `template` di `main` dengan kode seperti berikut:
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Dengan kode diatas kita membuat tampilan untuk menambahkan Item dalam form yang sudah di generate oleh Django.

#### f) Mengedit file `homepage.html` seperti berikut:
```html
{% extends 'base.html' %}

{% block content %}

<h1>WELCOME TO QEMUL OLSHOP!!!</h1>

<h3>Nama Aplikasi: </h3>
<p>{{Nama_Aplikasi}}</p>

<h3>Nama: </h3>
<p>{{Nama}}<p>

<h3>Kelas: </h3>
<p>{{Kelas}}<p>

<h3>Kamu memiliki {{jumlah_jenis}} item dengan total {{jumlah_barang}} buah</h3>

<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:add_item' %}">
    <button>
        Add New Item
    </button>
</a>

{% endblock content %}
```
Dengan kode diatas kita bisa memvisualkan data kita dengan tampilan tabel dan ada tombol yang bisa mengantarkan kita untuk menambahkan data kita.

### 2. Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Membuat fungsi `show_xml, show_json, show_xml_by_id, show_json_by_id` ditambah dengan mengedit `show_main` yang telah dilakukan dipembuatan forms diatas pada `views.py` di `main`
```py
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
```
Dari masing fungsi-fungsi diatas kita membuat export data base yang kita punya sesuai format yang diinginkan bisa XML, JSON, atau dalam bentukan website HTML.

### 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Mengimport fungsi di `views.py` pada `main` dan membuat route path di `urls.py` di `main`.

```py
from django.urls import path
from main.views import show_main,add_item,show_xml,show_xml_by_id,show_json,show_json_by_id

app_name = "main"

urlpatterns = [
    path("", show_main, name = "show_main"),
    path("add-item",add_item, name="add_item"),
    path("xml",show_xml, name="show_xml"),
    path("xml/<int:id>/",show_xml_by_id, name="show_xml_by_id"),
    path("json",show_json, name="show_json"),
    path("json/<int:id>/",show_json_by_id, name="show_json_by_id")
]
```
Dari kode diatas jadinya jika ada path dari website utama akan ke arah fungsi untuk menampikan database sesuai format yang diinginkan.

## E. Screenshot Postman HTML, JSON, XML, JSON by ID, XML by ID
#### 1. SS Postman HTML
<img src = dokumen_tambahan\show_html.jpg>

#### 2. SS Postman JSON
<img src = dokumen_tambahan\show_json.jpg>

#### 3. SS Postman JSON by ID
<img src = dokumen_tambahan\show_json_id.jpg>

#### 4. SS Postman XML
<img src = dokumen_tambahan\show_xml.jpg>

#### 5. SS Postman XML by ID
<img src = dokumen_tambahan\show_xml_id.jpg>

<br>

# TUGAS 2 PBP


<hr>

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


