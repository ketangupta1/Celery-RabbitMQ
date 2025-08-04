import time

from celery import Celery

app = Celery('tasks', broker = 'pyamqp://guest@localhost//', backend='rpc://')

@app.task
def add(x,y):
    print("Task received in celery")
    print(f"Adding {x} + {y}")
    return x+y