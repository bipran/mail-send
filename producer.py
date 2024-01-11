import pika
import csv
import json
import pandas as pd


def read_xslx_file():
    df = pd.read_excel('path to xlxs file', engine='openpyxl')
    senders = [
        'rabee.tmg123@gmail.com',
        'rabindra.tamang@codehimalaya.net',
        'pascalrai66@gmail.com',
        'pascal.rai@codehimalaya.net',
        'dristi.sigdel@codehimalaya.net',
        'sigdeldristi@gmail.com',
        'medristee@gmail.com',
        'np03a190166@heraldcollege.edu.np',
        'sujan.neupane@codehimalaya.net',
        'nirajkaranjeet.codehimalaya@gmail.com',
        '018bscit023@sxc.edu.np',
        'medristee1@gmail.com',
        # new added value.
        # 'np03a19016@heraldcollege.edu.np',
        # 'sujan.neupane3@codehimalaya.net',
        # 'nirajkaranjeet.codehimalaya3@gmail.com',
        # '018bscit0234@sxc.edu.np'
    ]
    df['sender'] = ''
    for i, _ in df.iterrows():
        sender_value = senders[i % len(senders)]
        try:
            if df['sender'].value_counts()[sender_value]>=2000:
                continue
            else:
                df.at[i, 'sender'] = sender_value
        except KeyError:
            df.at[i, 'sender'] = sender_value
        # print(df['sender'].value_counts()[row['sender']])
    # print(df)
    sender_counts = df['sender']
    print(sender_counts)
    print(df['sender'].value_counts()[''])
    df.to_csv('test.csv')
    return 

# read_xslx_file()

class RabbitMq:
    """"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    
    def load_data_to_producer(self):
        batch_size = 2
        batch = []
        with open('path to csv file', 'r') as f:
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