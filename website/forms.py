from django import forms

class SearchForm(forms.Form):
    search-text = forms.CharField(label='Search', max_length=150)