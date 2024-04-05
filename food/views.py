from django.shortcuts import render

# Create your views here.
def biriyani(request):
    return render(request,'biriyani.html')
def biriyani_response(request):
    return render(request,'biriyani_response.html')
