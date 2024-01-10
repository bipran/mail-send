# from datetime import datetime

# sender_info = {
#     "prabin@yopmail.com":{
#         "password":"uhwt njqh lhhk rssl",
#         "total_email_sent":0,
#         "today_date": datetime.now(),
#         "name": "Prabin Pandey"
#     },
# }

import csv

# Sample list of dictionaries
data = [
#     {"first_name": "John", "last_name": "Doe", "email": "rabee.tmg123@gmail.com"},
#     {"first_name": "Jane", "last_name": "Smith", "email": "rabindra.tamang@codehimalaya.net"},
    {"first_name": "Alice", "last_name": "Johnson", "email": "pascal.rai@codehimalaya.net"},
    # {"first_name": "Alice", "last_name": "Johnson", "email": "dristi.sigdel@codehimalaya.net"},
    
    # {"first_name": "John", "last_name": "Doe", "email": "sigdeldristi@gmail.com"},
    # {"first_name": "Jane", "last_name": "Smith", "email": "medristee@gmail.com"},
    # {"first_name": "Alice", "last_name": "Johnson", "email": "np03a190166@heraldcollege.edu.np"},
    {"first_name": "Alice", "last_name": "Johnson", "email": "sujan.neupane@codehimalaya.net"},
]

# Specify the CSV file name
csv_file = "reveiver.csv"

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "email"])
    
    # Write header
    writer.writeheader()
    
    # Write data
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been generated.")

