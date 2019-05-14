from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DeliveryTaskForm
from .models import DeliveryTask


def task_create(request):
    if request.user.is_store_manager:
        form = DeliveryTaskForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                task = form.save(commit=False)
                task.created_by = request.user
                task.save()
                messages.success(request, 'Task successfully Created')
                return redirect(reverse('delivery:create'))
        return render(request, 'delivery/create_task.html', {'form': form})
    else:
        raise PermissionDenied
