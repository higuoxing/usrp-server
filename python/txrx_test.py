import zmq
import time
import json

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send(b"""
{
  "id": 1,
  "type": "CONF",
  "payload": [
     {"key": "tx_rate", "val": "20000000"},
     {"key": "rx_rate", "val": "20000000"},
     {"key": "tx_bandwidth", "val": "20000000"},
     {"key": "rx_bandwidth", "val": "20000000"},
     {"key": "tx_freq", "val": "2500000000"},
     {"key": "rx_freq", "val": "2500000000"},
     {"key": "tx_antenna", "val": "TX/RX"},
     {"key": "rx_antenna", "val": "RX2"},
     {"key" : "rx_sample_per_buffer", "val":  "300000"},
     {"key" : "tx_sample_per_buffer", "val" : "300000"},
     {"key" : "clock_source", "val": "internal"}
   ]
}""")

# Get the reply.
message = socket.recv()
print(str(message.decode()), flush=True)

socket.send(b"""
{
  "id": 2,
  "type": "WORK",
  "payload": [
    {"key": "funcname", "val" : "launch_sample_to_file"},
    {"key": "filename", "val" : "/tmp/mysine.data"}
   ]
}""")

# Get the reply.
message = socket.recv()
print(str(message.decode()), flush=True)

time.sleep(0.1)

socket.send(b"""
{
 "id": 3,
  "type": "WORK",
  "payload": [
    {"key": "funcname", "val" : "launch_sample_from_file"},
    {"key": "filename", "val" : "/tmp/sine.data"}
   ]
}""")

# Get the reply.
message = socket.recv()
print(str(message.decode()), flush=True)

#time.sleep(1)

socket.send(b"""
{
  "id": 4,
  "type": "WORK",
  "payload": [
    {"key": "funcname", "val" : "shutdown_sample_to_file"}
   ]
}""")

# Get the reply.
message = socket.recv()
print(str(message.decode()), flush=True)