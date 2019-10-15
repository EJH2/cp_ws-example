import time
from random import random

from celery import shared_task
from celery_progress.backend import ProgressRecorder, WebSocketProgressRecorder


@shared_task(bind=True)
def http_task(self, number):
    progress_recorder = ProgressRecorder(self)
    for i in range(number):
        time.sleep(.1)
        progress_recorder.set_progress(i+1, number)
    return random()*1000


@shared_task(bind=True)
def http_error_task(self, number):
    progress_recorder = ProgressRecorder(self)
    for i in range(number):
        time.sleep(.1)
        progress_recorder.set_progress(i+1, number)
        if i == int(number/2):
            raise StopIteration('We broke it!')
    return random()*1000


@shared_task(bind=True)
def ws_task(self, number):
    progress_recorder = WebSocketProgressRecorder(self)
    for i in range(number):
        time.sleep(.1)
        progress_recorder.set_progress(i+1, number)
    return random()*1000


@shared_task(bind=True)
def ws_error_task(self, number):
    progress_recorder = WebSocketProgressRecorder(self)
    for i in range(number):
        time.sleep(.1)
        progress_recorder.set_progress(i+1, number)
        if i == int(number/2):
            raise StopIteration('We broke it!')
    return random()*1000

