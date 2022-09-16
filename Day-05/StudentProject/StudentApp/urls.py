from django.urls import path
from StudentApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('ab/',views.about,name="abt"),
]