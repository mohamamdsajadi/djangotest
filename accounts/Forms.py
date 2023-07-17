from dataclasses import field
from django.contrib.auth import get_user_model  
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    class Meta :
        fields = (  "username" , "email" , "display_name"  )
        model = get_user_model()
    def     __init__(self, *args, **kwargs) :
        
        super().__init__(*args, **kwargs)
        self.fields["username"].lable = "mohammadsajadi"
        self.fields["email"].lable = "mohammadsajadi@gmail.com"