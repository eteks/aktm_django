from django import forms

class KeyStatusForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)
