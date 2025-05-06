from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

@login_required
def profile_view(request):
	"""顯示個人資料"""
	return render(request, 'users/profile.html', {
		'user': request.user
	})

@login_required
def profile_edit(request):
	"""編輯個人資料"""
	user = request.user
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, '個人資料已更新成功！')
			return redirect('profile')
	else:
		form = ProfileForm(instance=user)
	
	return render(request, 'users/profile_edit.html', {
		'form': form
	})
