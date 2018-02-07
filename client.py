#!/usr/bin/env python

## From:
## https://wiki.python.org/moin/TcpCommunication

import socket
import csv, json
import sys

with open('testdata.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = list(csvreader)

#print(len(csvreader[0]))

tx_data = json.dumps(csvreader)
tx_data = tx_data.encode()
print(sys.getsizeof(tx_data))

TCP_IP = '127.0.0.1'
TCP_PORT = 5025

BUFFER_SIZE = 2097152

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(tx_data)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
