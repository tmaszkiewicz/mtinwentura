from django import forms

class indeksForm(forms.Form):
    barcode = forms.CharField(widget=forms.TextInput(attrs={'onfocusout': 'focus()', 'onKeyUp': 'submit();','size': 10, 'autofocus': True}))
