from django.shortcuts import render

# Create your views here.
def btst(request):
	return render(request,'ht/boot.html')

def gy(request):
	if request.method == "POST":
		us = request.POST['u']
		em = request.POST['e']
		return render(request,'ht/details.html',{'username':us,'email':em})
	return render(request,'ht/rg.html')