from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home_drive(request):
    #return HttpResponse("Hello World")
    return render(request,'Drive/index-alt.html')