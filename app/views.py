from django.shortcuts import render

# Create your views here.
def panda(request):
    return render(request,'panda.html')

def pavi(request):
    return render(request,'pavi.html')

def pi5(request):
    return render(request,'pi5.html')
