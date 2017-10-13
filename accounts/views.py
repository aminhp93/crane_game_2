from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm

User = get_user_model()

def login_view(request):
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get('password')
		user = authenticate(email=email, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect("/")
	return render(request, "accounts/form.html", {"form":form, "title": title})


def register_view(request):
	next = request.GET.get('next')
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(email=user.email, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect("/")

	context = {
		"form": form,
		"title": title
	}
	return render(request, "accounts/form.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")