from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields =['title','mail', 'content']


        widgets = {
            'title': forms.TextInput(attrs={"class":"input-contact", "placeholder":"Nombre"}),
            'mail': forms.EmailInput(attrs={"class":"input-contact", "placeholder":"Correo Electronico"}),
            'content': forms.Textarea(attrs={"id":"contact-content"})
        }

        labels = {
            'title':'',
            'mail':'',
            'content':'',
        }