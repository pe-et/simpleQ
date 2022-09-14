from django.urls import path

from .views import (
    QueueListView,
    QueueDetailView,
    QueueUpdateView,
    QueueRemoveView,
    QueueCreateView,
)

urlpatterns = [
    path("<int:pk>/", QueueDetailView.as_view(), name="queue_detail"),
    path("<int:pk>/edit/", QueueUpdateView.as_view(), name="queue_edit"),
    path("<int:pk>/delete/", QueueRemoveView.as_view(), name="queue_remove"),
    path("new/", QueueCreateView.as_view(), name="queue_new"),
    path("", QueueListView.as_view(), name="queue_list"),
]
