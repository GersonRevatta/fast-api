import pika
from app.core.config import settings

def publish_message(event: str, payload: dict):
    try:
        connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
        channel = connection.channel()

        channel.queue_declare(queue="user_events", durable=True)

        message = f"Te mandaremos un correo. {event} correctamente: {payload}"

        channel.basic_publish(
            exchange="",
            routing_key="user_events",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),  # Hacer que el mensaje sea persistente
        )

        print(f"Published message: {message}")
        connection.close()
    except Exception as e:
        print(f"Error publishing message: {e}")
