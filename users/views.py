from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from  .forms import  CreatUserForm
from django.contrib import messages

# Create your views here.


def register(request):
	if request.method != 'POST':
		form = CreatUserForm()
	else:
		form = CreatUserForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Acount was Created for' + user)

			login(request, new_user)
			return redirect('BlogApp:index')
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def loginpage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('BlogApp:index')

		context = {}
		return render(request, 'registration/login.html')
