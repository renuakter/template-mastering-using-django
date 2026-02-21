from django.shortcuts import render

# Create your views here.
def basepage(req):
    return render(req,"master/base.html")