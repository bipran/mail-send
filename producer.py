import pika
import csv
import json
    

class RabbitMq:
    """"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    
    def load_data_to_producer(self):
        batch_size = 2
        batch = []
        with open('/home/prabin/code_project/send_mail/reveiver.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append(row)
                if len(batch) == batch_size:
                    # Convert the batch to a JSON string
                    message = json.dumps(batch)
                    # Publish the batch to the queue
                    self.channel.basic_publish(exchange='', routing_key='email_queue', body=message)
                    # Clear the batch
                    batch = []
            
            # Don't forget the last batch if it's not full
            if batch:
                message = json.dumps(batch)
                self.channel.basic_publish(exchange='', routing_key='email_queue', body=message)
rabbitmq = RabbitMq()
rabbitmq.load_data_to_producer()

    
    