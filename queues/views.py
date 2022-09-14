from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Queue


class QueueListView(LoginRequiredMixin, ListView):
    model = Queue

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by("date")

    paginate_by = 2
    template_name = "queue_list.html"


class QueueDetailView(LoginRequiredMixin, DetailView):
    model = Queue
    template_name = "queue_detail.html"


class QueueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Queue
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "notes",
    )
    template_name = "queue_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class QueueRemoveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Queue
    template_name = "queue_remove.html"
    success_url = reverse_lazy("queue_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class QueueCreateView(LoginRequiredMixin, CreateView):
    model = Queue
    template_name = "queue_new.html"
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "notes",
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
