from django import forms
from django.forms.widgets import TextInput

class ContactForm(forms.Form):
    name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class':'input-block-level', 'placeholder':'your name', 'type':'text', 'name':'name', 'id':'name'}))
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'class':'input-block-level', 'placeholder':'your email', 'type':'email', 'id':'mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'input-block-level', 'placeholder':'your message', 'id':'msg', 'rows':'6'}), label="")
    
