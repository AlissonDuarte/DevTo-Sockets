from socketapp import models
from django.shortcuts import render

def test(request):
    r = models.Random.objects.create(text = "test")
    data = {"text":models.Random.objects.first().text}
    return render(request, 'test.html', context = data)
