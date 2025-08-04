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


