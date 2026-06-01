from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from .forms import RegisterForm

from django.contrib.auth.views import LoginView

from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")


def register_view(request):
    """
    Register New User
    """

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration successful."
            )

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )