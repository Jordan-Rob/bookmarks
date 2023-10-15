from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            user = authenticate(username=clean_form["username"], password=clean_form["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Logged in")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login Details Supplied!")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})