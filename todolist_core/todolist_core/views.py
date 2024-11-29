# views.py
from django.http import JsonResponse
from .tasks import add, long_task
from celery.result import AsyncResult


def add_view(request):
    result = add.delay(4, 4)  # вызов асинхронной задачи
    return JsonResponse({'task_id': result.id, 'status': 'Task Submitted'})


def long_task_view(request):
    result = long_task.delay()  # вызов асинхронной задачи
    return JsonResponse({'task_id': result.id, 'status': 'Long Task Submitted'})


def check_task_status_view(request, task_id):
    result = AsyncResult(task_id)
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'status': 'Pending...'
        }
    elif result.state != 'FAILURE':
        response = {
            'state': result.state,
            'result': result.result
        }
    else:
        response = {
            'state': result.state,
            'status': str(result.info)  # Ошибка когда-нибудь сохранится в результат
        }
    return JsonResponse(response)
