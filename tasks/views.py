from django.shortcuts import render

from .tasks import http_task, ws_task


def http_view(request):
    print(1)
    result = http_task.delay(number=100)
    print(2)
    return render(request, 'http.html', context={'task_id': result.task_id})


def ws_view(request):
    print(2)
    result = ws_task.delay(number=100)
    print(3)
    return render(request, 'ws.html', context={'task_id': result.task_id})
