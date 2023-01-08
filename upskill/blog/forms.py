from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
     # Add any other fields you want to include in the form
