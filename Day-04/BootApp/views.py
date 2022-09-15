from django.shortcuts import render

# Create your views here.
def btst(request):
	return render(request,'ht/boot.html')

def gy(request):
	return render(request,'ht/rg.html')