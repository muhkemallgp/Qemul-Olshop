from django.forms import ModelForm
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['name'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'name', 
            'id':'name', 
            'type':'text', 
            'placeholder':'Nama Barang', 
            })
        
        self.fields['amount'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'amount', 
            'id':'amount', 
            'type':'number', 
            'placeholder':'Jumlah Barang', 
            'min':'0',
            })
        self.fields['description'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'description', 
            'id':'description', 
            'type':'text-area', 
            'placeholder':'Deskripsi Barang', 
            })   

class RegisterForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = ('username', 'password1', 'password2') 

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
        self.fields['password1'].widget.attrs.update({ 
            'class': 'input-field', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'input-field', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Validate password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 