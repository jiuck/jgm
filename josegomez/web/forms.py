from django import forms 
 
class HelloForm(forms.Form): 
     subject = forms.CharField() 
     email = forms.EmailField() 
     message = forms.CharField(widget=forms.Textarea)