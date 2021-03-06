from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def signup(request):
	# if request.user.is_authenticated:
	# 	return redirect('/di_main_app/index/', permanent=False)

	registered = False
	if request.method =='POST':
		user_form = forms.UserForm(data= request.POST) 
		profile_form = forms.UserProfileInfoForm(data= request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit= False)
			profile.user = user

			profile.save()
			registered = True
			login(request, user)
			return redirect('/chat/', permanent=False)


		else :
			print(user_form.errors, profile_form.errors)

	else: 
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()

	return render(request, 'signup_form.html', context = {
		'user_form' : user_form,
		'profile_form' : profile_form, 
		'registered': registered
		})



def log_in(request):
	if request.user.is_authenticated:
		return redirect('/chat/', permanent=False)

	errors = False
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			clean_data = login_form.clean()
			user = authenticate(username=clean_data['username'], password=clean_data['password'])
			
			if user is not None:
				login(request, user)
				print('Logged In: {}'.format(user))
				return redirect('/chat/', permanent=False)
				
			else:
				errors = True
	else:
		login_form = forms.LoginForm()

	return render(request, 'login_form.html', {
			'login_form': login_form,
			'errors': errors,})



@login_required
def logging_out(request):
	print(request.user)
	logout(request)
	return redirect('/profile/login/')

