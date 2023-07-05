from django.shortcuts import render
#from django.http import HttpResponse
from django import forms
from django.urls import is_valid_path
import numpy as np

class DimForm(forms.Form):
    width = forms.DecimalField(min_value=0, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Width', 'autocomplete':'off'}))
    height = forms.DecimalField(min_value=0, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Height', 'autocomplete':'off'}))
    

def index(request):
    if request.method == "POST":
        form = DimForm(request.POST)
        if form.is_valid():
            w = float(form.cleaned_data["width"])
            h = float(form.cleaned_data["height"])
            ratio = w/h
            return render(request, "res/display.html", {
                "w" : w,
                "h" : h,
                "ratio" : ratio,
                "w_range" : np.arange(1921),
                "h_range" : np.arange(1081)
            })
        else:
            return render(request, "res/index.html", {
        "form" : DimForm
    })
    
    return render(request, "res/index.html", {
        "form" : DimForm
    })
