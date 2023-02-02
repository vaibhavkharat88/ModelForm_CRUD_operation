from django import forms
from .models import vaibhav

class Adddata(forms.ModelForm):
    name=forms.CharField( max_length=20, required=False)
    email=forms.EmailField(max_length=50, required=False)
    price=forms.DecimalField(max_digits=10,decimal_places=2, required=False)
    stock=forms.IntegerField()
    desc=forms.CharField(widget=forms.Textarea)


    class Meta:
        model=vaibhav
        fields=['name','email','price','stock','desc']
