from django.shortcuts import render

from .tasks import http_task, http_error_task, ws_task, ws_error_task


def index(request):
    return render(request, 'index.html')


def http_view(request):
    result = http_task.delay(number=100)
    return render(request, 'http.html', context={'task_id': result.task_id})


def http_error_view(request):
    result = http_error_task.delay(number=100)
    return render(request, 'http.html', context={'task_id': result.task_id})


def ws_view(request):
    result = ws_task.delay(number=100)
    return render(request, 'ws.html', context={'task_id': result.task_id})


def ws_error_view(request):
    result = ws_error_task.delay(number=100)
    return render(request, 'ws.html', context={'task_id': result.task_id})
