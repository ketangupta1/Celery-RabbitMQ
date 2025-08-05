from cel_tasks import first_task, second_task

# first_task.apply_async(("First task invoked",))
#
# second_task.apply_async(("Second task invoked",))

first_task.delay("First task invoked")
second_task.delay("Second task invoked")
