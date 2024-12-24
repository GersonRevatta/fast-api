#!/bin/bash

# Habilitar el plugin rabbitmq_delayed_message_exchange
rabbitmq-plugins enable rabbitmq_delayed_message_exchange

# Iniciar RabbitMQ
rabbitmq-server
