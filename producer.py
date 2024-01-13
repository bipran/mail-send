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
    # sender_counts = df['sender']
    df.to_csv('test.xlxx')
    return 

def chunk_and_save(input_csv, chunk_size, output_prefix):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Get the total number of rows in the DataFrame
    total_rows = df.shape[0]

    # Calculate the number of chunks needed
    num_chunks = (total_rows + chunk_size - 1) // chunk_size

    # Split the DataFrame into chunks
    chunks = [df.iloc[i*chunk_size:(i+1)*chunk_size] for i in range(num_chunks)]

    # Save each chunk to a separate CSV file
    for i, chunk in enumerate(chunks):
        output_filename = f"csv_chunk/{output_prefix}_chunk_{i + 1}.csv"
        chunk.to_csv(output_filename, index=False)
        print(f"Chunk {i + 1} saved to {output_filename}")

# chunk_and_save('/home/prabin/code_project/send_mail/test.csv', 10000,'new')

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
# rabbitmq.load_data_to_producer()