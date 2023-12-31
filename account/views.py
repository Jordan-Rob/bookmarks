from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            user = authenticate(
                username=clean_form["username"], password=clean_form["password"]
            )

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
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            # create new user without saving
            new_user = user_form.save(commit=False)
            # set the password using set_password method
            new_user.set_password(user_form.cleaned_data["password"])
            # save the User object
            new_user.save()
            # create associated user profile
            Profile.objects.create(user=new_user)

            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request, 'account/edit.html', { 'user_form': user_form, 'profile_form': profile_form})
