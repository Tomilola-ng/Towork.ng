from django.urls import reverse
from django.contrib.auth import login
from .models import Profile
from users.forms import CustomUserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect 


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
    else:
        context = {
            'form': CustomUserCreationForm
        }
        return render(request, 'users/register.html', context ) 


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


def home(request):
    return render(request, "users/home.html")


class profileCreate(LoginRequiredMixin ,CreateView):
    model = Profile
    fields = ['picture','state','local_government','phone','gender','bio']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class profileUpdate(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model = Profile
    template_name = 'users/dashboard.html'
    fields = ['state','local_government','gender','bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Update Your Profile"
        return context