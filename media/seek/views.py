from django.views.generic import CreateView, DetailView, ListView
from .models import Seek
from django.contrib.auth.mixins import LoginRequiredMixin

class seekCreate(LoginRequiredMixin,CreateView):
    model = Seek
    fields = ['budget','job']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.state = self.request.user.profile.state
        form.instance.local_government = self.request.user.profile.local_government
        return super().form_valid(form)

class seekList(LoginRequiredMixin, ListView):
    model = Seek


class seekDetail(LoginRequiredMixin, DetailView):
    model = Seek