from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False, label='Your e-mail')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':'40', 'rows':'12'}))
    
class ShortContact(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':'25', 'rows':'8'}))