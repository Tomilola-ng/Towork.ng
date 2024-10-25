""" Seek Artisans Views """

from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from seek.models import Seek


class SeekCreate(LoginRequiredMixin, CreateView):
    """ Create a new Seek Instance """
    model = Seek
    fields = ['budget', 'job']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.state = self.request.user.profile.state
        form.instance.local_government = self.request.user.profile.local_government
        return super().form_valid(form)


class SeekList(LoginRequiredMixin, ListView):
    """ List all Seek Instances """
    model = Seek


class SeekDetail(LoginRequiredMixin, DetailView):
    """ Detail a specific Seek Instance """
    model = Seek
