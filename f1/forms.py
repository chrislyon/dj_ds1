from django import forms

class f1_form(forms.Form):
	your_name = forms.CharField(label='Ton Nom', max_length=100)
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	datcre = forms.DateField()
	cc_myself = forms.BooleanField(required=False)
