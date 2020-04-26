from django.shortcuts import render, redirect
import django.urls

from registration.forms import CustomUserForm


def create_user(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)

        success_url = django.urls.reverse('registration:login')

        if form.is_valid():
            form.save()
            return redirect(success_url)


    return render(request, 'registration.html', {'form':form})

def login_view(request):
    return render(request, 'login.html', {})
