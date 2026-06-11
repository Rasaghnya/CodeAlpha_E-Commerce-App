from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from .forms import RegisterForm, LoginForm

from django.contrib.auth.views import LoginView

from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True

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