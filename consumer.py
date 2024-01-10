import pika
import json
import time
from send_mail_to import send_html_mail
from logger_config import logging

def callback(ch, method, properties, body):
    logging.mail_send_logger.info("[received: ] Mail list fetched fro server.")
    # Parse the JSON message
    data = json.loads(body)
    for v in data:
        if 'email' in v:
            name = v.get('first_name')+" "+ v.get('last_name')
            receipant = [v.get('email')]
            send_html_mail(receipant, name)
            time.sleep(2)
    logging.mail_send_logger.info(f"[Successfull: ] Mail successfully sent.")
    time.sleep(1)

# Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='email_queue')

# Set up the consumer
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

logging.mail_send_logger.info('[Waiting: ] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()