from socketapp import models
from django.shortcuts import render

def test(request):
    return render(request, 'test.html', context = {})
