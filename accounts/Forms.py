from dataclasses import field
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    class Meta :
        fields = (  "username" , "email"   , 'first_name' , 'last_name')
        model = User
    def     __init__(self, *args, **kwargs) :
        
        super().__init__(*args, **kwargs)
        self.fields["username"].lable = "mohammadsajadi"
        self.fields["email"].lable = "mohammadsajadi@gmail.com"