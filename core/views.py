from django.shortcuts import render, redirect
from .forms import SignUpFrom
from django.contrib.auth import login


def front_page(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpFrom

    return render(request, 'core/signup.html', {'form': form})