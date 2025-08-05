from celery import Celery

app = Celery('cel_tasks', broker="pyamqp://guest@localhost//", backend='rpc://')

app.conf.task_default_queue = 'first'

@app.task(queue = 'first')
def first_task(incoming_message):
    print(incoming_message)

@app.task(queue = 'second')
def second_task(incoming_message):
    print(incoming_message)

