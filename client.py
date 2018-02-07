#!/usr/bin/env python

## From:
## https://wiki.python.org/moin/TcpCommunication

## Very very basic client to ping an example array to the nn server

import socket
import csv, json
import sys


## Open CSV
with open('testdata.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = list(csvreader)

#print(len(csvreader[0]))


## Crunch it into JSON format
tx_data = json.dumps(csvreader)
tx_data = tx_data.encode()
print(sys.getsizeof(tx_data))


## Localhost for now
TCP_IP = '127.0.0.1'
TCP_PORT = 5025


## 2M buffer to give a bit of room
BUFFER_SIZE = 2097152


## Set up socket and connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#TX
s.send(tx_data)
#RX
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
