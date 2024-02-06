from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subiect = forms.CharField()
    mesaj = forms.CharField(widget=forms.Textarea())
    
    
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
