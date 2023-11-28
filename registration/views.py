from django.shortcuts import render, redirect
from .forms import CreateRegistrationForm, UpdateUserForm, UpdateProfileForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created! You can now log in.')
            return redirect('login-user')
    else:
        form = CreateRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')


def profile(request):
    return render(request, 'registration/profile.html')


def profile_update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'registration/profile_update.html', context)
