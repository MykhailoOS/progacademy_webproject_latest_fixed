from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from furni.models import Checkout
from .forms import OrderForm, EditOrderForm
from django.urls import reverse_lazy


# Create your views here.

# @login_required(login_url='/login/')
# def index(request):
#     return render(request, 'manager.html')


class ManagerCheck(UserPassesTestMixin):
    """
    Manager check test
    """
    def test_func(self):
        return self.request.user.groups.filter(name='managers').exists()


class IndexView(LoginRequiredMixin, ManagerCheck, ListView):
    """
    Index view of manager page
    """
    template_name = 'manager.html'
    model = Checkout
    login_url = '/login/'
    context_object_name = 'reservations'

    def queryset(self):
        return Checkout.objects.filter(is_approved=False).order_by('-created_at')


class IndexOrderView(LoginRequiredMixin, ManagerCheck, UpdateView):
    """
    Working with editor reservation page
    """
    template_name = 'approve.html'
    login_url = '/login/'
    model = Checkout
    form_class = EditOrderForm
    success_url = reverse_lazy('manager:index')