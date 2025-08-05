# Celery-RabbitMQ
Running background jobs using celery and rabbitmq
## Rabbitmq installation and setup
- To install tabbitmq:
  
      sudo apt-get install rabbitmq-server
- To start the rabbitmq server:

      sudo service rabbitmq-server start
- To see the rabbitmq dashboard(web UI), you need to enable and access Rabbitmq management pligin
- To enable management plugin:

      sudo rabbitmq-plugins enable rabbitmq_management
- Restart the rabbitmq server:

      sudo service rabbitmq-server restart
-  Open the dashboard in your browser go to:

        http://localhost:15672

## Celery installation and running:
- To install celery:

      pip install celery
- Flow is like:
  - You will send the task to rabbitmq Q.
  - Rabbitmq stores the message(the task info) in the queue.
  - When rabbitmq has a messagee:
      - Celery receives it
      - Celery executes the python prgm inside its own process
      - It then sends result back to the result backend(Optional).
      
- Overview:
    - Rabbitmq: Just a middleman(queue/message broker).
    - Celery broker: Does the actual work/executes function.
    - App: Only sends the task(doesn't do the work).

- Why do you need result backend:
    - Celery uses a backend to store and fetch task results. Without one, result.get() won't work bcz there is nowhere to get the results from.
    - Common backend options: rpc(Lightweight, works well locally), redis(Popular and fast), database(Slower used for testing).
