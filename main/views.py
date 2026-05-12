from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task, STATUS
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    login_url = 'auth'

    def get(self, request):
        statuses = [status[0] for status in STATUS]
        tasks = Task.objects.filter(user=request.user)
        context = {
            'statuses': statuses,
            'tasks': tasks
        }
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST.get('title'),
            details=request.POST.get('details'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline') if request.POST.get('deadline') else None,
            user=request.user,
        )
        return redirect('home')


class TaskUpdateView(LoginRequiredMixin, View):
    login_url = 'auth'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        statuses = [status[0] for status in STATUS]
        context = {
            'task': task,
            'statuses': statuses,
        }
        return render(request, 'edit.html', context)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.title = request.POST.get('title')
        task.details = request.POST.get('details')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline') if request.POST.get('deadline') else None
        task.save()
        return redirect('home')


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = 'auth'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('home')