""" Workers Views """

from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from workers.models import Worker


class CreateWorker(LoginRequiredMixin, CreateView):
    """ Create a new Worker Instance """
    model = Worker
    template_name = 'users/dashboard.html'
    fields = ['job',]

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Change Job Description"
        return context


class WorkerUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Update a Worker Instance """
    model = Worker
    template_name = 'users/dashboard.html'
    fields = ['job',]

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        worker = self.get_object()
        if self.request.user.profile.worker == worker:
            return True
        return False

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Change Job Description"
        return context
