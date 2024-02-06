from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subiect = forms.CharField()
    mesaj = forms.CharField(widget=forms.Textarea())