from django.urls import path
from StudentApp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('ab/',views.about,name="abt"),
	path('reg/',views.register,name="rg"),
	path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]