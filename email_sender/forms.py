from django import forms

class EmailForm(forms.Form):
    sender = forms.EmailField()
    receiver = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)
