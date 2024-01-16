import pika
import json
import time
from send_mail_to import send_html_mail
from logger_config import logging

def callback(ch, method, properties, body):
    logging.mail_send_logger.info("[received: queue 1] Mail list fetched from server.")
    # Parse the JSON message
    data = json.loads(body)
    for v in data:
        if 'Email' in v:
            name = v.get('First name')+" "+ v.get('Last name')
            receipant = [v.get('email')]
            # send_html_mail(receipant, name)
            time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # logging.mail_send_logger.info(f"[ACKNOWLEDGED.........: ] Mail successfully sent.")
    time.sleep(1)

def callback_queue_1(ch, method, properties, body):
    logging.mail_send_logger.info("[received: queue 2] Mail list fetched from server.")
    data = json.loads(body)
    for v in data:
        if 'Email' in v:
            name = v.get('First name')+" "+ v.get('Last name')
            receipant = [v.get('email')]
            send_html_mail(receipant, name)
            time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # logging.mail_send_logger.info(f"[ACKNOWLEDGED.........: ] Mail successfully sent.")
    time.sleep(1)
# Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='email_queue_1')

# Set up the consumer
channel.basic_consume(queue='email_queue_1', on_message_callback=callback, auto_ack=False)
# channel.basic_consume(queue='email_queue_2', on_message_callback=callback_queue_1, auto_ack=False)
# channel.basic_consume(queue='email_queue_3', on_message_callback=callback_queue_2, auto_ack=False)

logging.mail_send_logger.info('[Waiting: ] Waiting for messages from. To exit press CTRL+C')
channel.start_consuming()