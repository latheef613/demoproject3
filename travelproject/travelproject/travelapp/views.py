from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class Httpresponse:
    pass


def demo(request):

    return render(request,'index.html')






