""" User Views """

from django.urls import reverse
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect

from users.models import Profile
from users.forms import CustomUserCreationForm


def register(request):
    """ Register a new user """
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
        return render(request, 'users/register.html', context)


@login_required
def dashboard(request):
    """ User Dashboard """
    return render(request, 'users/dashboard.html')


def home(request):
    """ Home Page """
    return render(request, "users/home.html")


class ProfileCreate(LoginRequiredMixin, CreateView):
    """ Create a new Profile """
    model = Profile
    fields = ['picture', 'state', 'local_government', 'phone', 'gender', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Update a Profile """
    model = Profile
    template_name = 'users/dashboard.html'
    fields = ['state', 'local_government', 'gender', 'bio']

    def form_valid(self, form):
        """ Save the form """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Test if the user is the same as the profile """
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

    def get_success_url(self):
        """ Redirect to the dashboard """
        return reverse('dashboard')

    def get_context_data(self, *args, **kwargs):  # pylint: disable=unused-argument
        """ Add the text to the context """
        context = super().get_context_data(**kwargs)
        context['text'] = "Update Your Profile"
        return context
