from django.shortcuts import render

# Create your views here.
def cocacola(request):
    return render(request,'cocacola.html')
def cocacola_response(request):
    return render(request,'cocacola_response.html')
