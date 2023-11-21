from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CreateRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = CreateRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)
