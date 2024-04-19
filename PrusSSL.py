import os
import csv
import smtplib
import ssl
#from dotenv import load_dotenv

#load_dotenv()

body="""
Hello coder;

Welcome {name} to code and share;
We're happy to inform you that you're selected in the {department} department;

Cordially;
"""

from_address = os.getenv('SENDER')
password = os.getenv('PSWD')

# The default context of ssl validates the host name and its certificates and optimizes the security of the connection.
#context = ssl.create_default_context()

# Creating a connection to SMTP server for gmail
port = 465  # For SSL
with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login(from_address, password)
    #server.set_debuglevel(1)
    # Sending multiple custom emails ( data from a csv file )
    with open("contact.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, dep in reader:
            server.sendmail(from_address, to_addrs=email, msg=body.format(name=name, department=dep))
