from django.shortcuts import render, redirect
from .forms import CreateRegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
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
