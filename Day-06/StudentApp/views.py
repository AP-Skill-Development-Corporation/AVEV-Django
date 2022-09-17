from django.shortcuts import render,redirect
from .forms import UsregForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		g = UsregForm(request.POST)
		if g.is_valid():
			g.save()
			messages.success(request,"User Created Successfully")
			return redirect('/login')
	g = UsregForm()
	return render(request,'html/reg.html',{'k':g})
