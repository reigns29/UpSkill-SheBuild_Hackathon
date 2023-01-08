from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length = 122)
    email = forms.EmailField(max_length = 200)
    password = forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.username



