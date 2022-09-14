from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wel(request):
	return HttpResponse("Welcome to APSSDC Program")

def dt(rt,un):
	return HttpResponse(f"Hi Welcome {un}")

def stdetails(request,sage,stn):
	return HttpResponse(f"<h3>Hi Welcome {stn}<br/>Your age is: {sage}</h3>")

def edetails(r,eid,ename,esal=2500):
	return HttpResponse(f"<h3>Employee Name: <span style='color:green'>{ename}</span><br/>Employee Salary: {esal}<br/>Employee Id: <span style='color:red'>{eid}</span>")

def dgp(request,tn):
	return HttpResponse(f"<html><head><title>Demo</title></head><body><h3>Welcome {tn}</h3></body></html>")

def vg(request,n,y):
	return HttpResponse(f"<html><head><title>Demo</title><script>alert('Hi Welcome {n}');</script></head><body><h3>Welcome {y}</h3></body></html>")

def bk(request):
	return render(request,'demo.html')