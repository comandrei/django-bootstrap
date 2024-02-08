from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError

from .models import Produs

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subiect = forms.CharField(label="Subiectul tau")
    mesaj = forms.CharField(widget=forms.Textarea())
    trimite_copie = forms.BooleanField(required=False)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("@gmail.com"):
            raise ValidationError("Email invalid!")
        return email
    
    
class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(None, username=username, password=password)
        if user is  None:
            raise ValidationError('Nu exista User-ul')
        else:
            self.authenticate_user = user
        return self.cleaned_data
    
class ProdusForm(forms.ModelForm):
    class Meta:
        model = Produs
        fields = "__all__"

