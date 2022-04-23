from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from . import forms
from django.contrib import messages
# Create your views here.

def homepage(request):
	if request.method == 'POST':
		form = forms.FeedbackForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			orphanage = form.save()
			messages.success(request, f"Feedback Submitted Successfully!!!")
		else:
			messages.error(request, "Something Went Wrong")

	form = forms.FeedbackForm
	events = Event.objects.all()
	context = {'events':events[0:3], 'form':form}
	return render(request=request, template_name = "main/home.html", context = context)


def logout_request(request):
	logout(request)
	messages.info(request, "You are logged out.")
	return redirect("main:homepage")

def login_request(request):
	next_page = None
	
	if request.method == 'GET':
		next_page = request.GET.get('next')
	if next_page != None:
		messages.error(request, "Need to login first")		

	print("Next PAGE IS :: ")
	print(next_page)

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			uname = form.cleaned_data.get('username')
			pwd = form.cleaned_data.get('password')
			user = authenticate(username=uname, password=pwd)
			if user is not None:
				login(request, user)
				messages.info(request, "Successfully logged In")
				
				if next_page == None:
					return redirect("main:homepage")					
				else:
					return redirect("main:"+next_page[1:])
			else: 
				messages.error(request, "Credentails are not Valid.")
		else: 
				messages.error(request, "Something went wrong")
	
	form = AuthenticationForm
	context = {"form":form}
	return render(request, "main/login.html", context)


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		pwd = request.POST.get('password1')
		pwd2 = request.POST.get('password2')
		if pwd != pwd2:
			messages.error(request, "Passwords do not match")

		if form.is_valid():
			fname = request.POST.get('first_name')
			lname = request.POST.get('last_name')
			uname = request.POST.get('username')
			email = request.POST.get('email')
			

			if pwd != pwd2:
				messages.error(request, "Passwords do not match")
				# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			else:
				user = User.objects.create_user(uname, email, pwd)
				user.first_name = fname
				user.last_name = lname
				user.save()

				messages.success(request,"User Register Successfully")

				login(request, user)
				messages.info(request, f"You are logged in as {uname}")
				return redirect("main:homepage")

		else:
			for msg in form.error_messages:
				messages.error(request, f"{form.error_messages[msg]}")


	form = forms.SignUpForm
	context = {"form":form}
	return render(request=request, 	
				  template_name="main/register.html", 
				  context = context)


@login_required(login_url="/login")
def about_us(request):
	return render(request, 'main/aboutUs.html')

@login_required(login_url="/login")
def orphanages(request):
	orphanages = Orphanage.objects.all()
	context = {'orphanages': orphanages}
	return render(request, "main/orphanages.html", context)

@login_required(login_url="/login")
def events(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, "main/events.html",context)


def orphanage_details(request, id):
	orpng = Orphanage.objects.get(id=id)
	feedbacks = Feedback.objects.filter(feedback_for=orpng)
	events = Event.objects.filter(organised_by=orpng)
	children = Orphan.objects.filter(admit_to = orpng)
	context = {"orp":orpng, "events":events, 'children':children,'feedbacks':feedbacks}
	print(orpng)
	return render(request, "main/orpng_details.html", context)


def register_orphanage(request):
	if request.method == 'POST':
		form = forms.OrphanageForm(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			orphanage = form.save()
			messages.success(request, f"Orphanage Register Successfully")
			return redirect("main:orphanages")
		else:
			messages.error(request, "Something Went Wrong")

	form = forms.OrphanageForm
	context = {'form':form}
	return render(request, "main/orphanage_registration.html",context)

def admit_orphan(request):
	if request.method == 'POST':
		form = forms.OrphanForm(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			orphanage = form.save()
			messages.success(request, f"Admission Request Sent please bring the child to the {form.cleaned_data.get('admit_to')}")
			return redirect("main:homepage")
		else:
			messages.error(request, "Something Went Wrong")

	form = forms.OrphanForm
	context = {'form':form}
	return render(request, "main/admit_orphan.html",context)

def adoption(request):
	return render(request, 'main/adoption.html')
