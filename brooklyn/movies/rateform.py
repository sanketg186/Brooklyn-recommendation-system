from django import forms



class RateForm(forms.Form):
    user = forms.CharField()
    movie_title =forms.CharField()
    rating =forms.IntegerField()