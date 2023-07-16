from dataclasses import field
from django.contrib.auth import  get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    class Meta :
        fields = ("username" , "email" , "password" , "password2")
        model = get_user_model
    def     __init__(self, *args, **kwargs) :
        
        super().__init__(*args, **kwargs)
        super.fields["username"].lable = "username"
        super.fields["email"].lable = "email address"