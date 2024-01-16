import pika
import csv
import json
import pandas as pd


def read_xslx_file():
    df = pd.read_excel('path to xlxs file', engine='openpyxl')
    senders = []
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
    # empty_salary_count = df['sender'].isna().sum()
    df_removed = df[df['sender'].isnull()]
    df = df[df['sender'].notnull()]
    if df_removed.shape[0]>0:
        df_removed.to_csv('path to/csv_chunk/csv_empty_sender_info.csv', index=False)

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
    # channel.queue_declare(queue='email_queue')
    
    def load_data_to_producer_1(self, path):
        batch_size = 2
        batch = []
        self.channel.queue_declare(queue='email_queue_1')
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append(row)
                if len(batch) == batch_size:
                    # Convert the batch to a JSON string
                    message = json.dumps(batch)
                    # Publish the batch to the queue
                    self.channel.basic_publish(exchange='', routing_key='email_queue_1', body=message)
                    # Clear the batch
                    batch = []            
            # Don't forget the last batch if it's not full
            if batch:
                message = json.dumps(batch)
                self.channel.basic_publish(exchange='', routing_key='email_queue_1', body=message)

    def load_data_to_producer_2(self, path):
        batch_size = 2
        batch = []
        self.channel.queue_declare(queue='email_queue_2')
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append(row)
                if len(batch) == batch_size:
                    # Convert the batch to a JSON string
                    message = json.dumps(batch)
                    # Publish the batch to the queue
                    self.channel.basic_publish(exchange='', routing_key='email_queue_2', body=message)
                    # Clear the batch
                    batch = []
            
            # Don't forget the last batch if it's not full
            if batch:
                message = json.dumps(batch)
                self.channel.basic_publish(exchange='', routing_key='email_queue_2', body=message)

    def load_data_to_producer_3(self, path):
        batch_size = 2
        batch = []
        self.channel.queue_declare(queue='email_queue_3')
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append(row)
                if len(batch) == batch_size:
                    # Convert the batch to a JSON string
                    message = json.dumps(batch)
                    # Publish the batch to the queue
                    self.channel.basic_publish(exchange='', routing_key='email_queue_3', body=message)
                    # Clear the batch
                    batch = []
            
            # Don't forget the last batch if it's not full
            if batch:
                message = json.dumps(batch)
                self.channel.basic_publish(exchange='', routing_key='email_queue_3', body=message)

if __name__ == "__main__":
    rabbitmq = RabbitMq()
    
    
    rabbitmq.load_data_to_producer_1('path to/new_chunk_1.csv')
    # rabbitmq.load_data_to_producer_2('path to/new_chunk_2.csv')
    # rabbitmq.load_data_to_producer_3('path to/new_chunk_1.csv')
