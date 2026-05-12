from django.urls import path
from .views import HomeView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]