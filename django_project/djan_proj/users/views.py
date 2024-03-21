from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now login')
			return redirect('bincom-home')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})


def profile(request):
	return render(request, 'users/profile.html')