from django import forms

class konfi(forms.Form):

    konfiname = forms.CharField(label='konfi', max_length=13000)

class gd(forms.Form):

    kirche = forms.CharField(label='Kirche', max_length=13000)
    datum = forms.DateTimeField(label='Datum')