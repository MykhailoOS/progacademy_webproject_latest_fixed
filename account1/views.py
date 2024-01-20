from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForm


# Create your views here.

def logout_view(request):
    """
    Logout view with logout template
    """
    logout(request)
    return render(request, 'logout.html')


class RegisterViewUser(CreateView):
    """
    Register view with register template
    """
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


class LoginViewUser(LoginView):
    """
    Login view for user login
    """
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'
