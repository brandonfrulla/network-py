#!/usr/bin/env python3

import socket
import time
import threading 

from queue import Queue
socket.setdefaulttimeout(0.2)
print_lock = threading.Lock()

# establishes the target IP
target = input('Enter the host to be scanned: ')
target_ip = socket.gethostbyname(target)
print('Starting scan on host: ', target_ip)

def portscan(port):
    sock_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 'knocks' on each port
    try:
        connect = sock_stream.connect(target_ip, port)
        with print_lock:
            print(port, 'is open')
        connect.close()
    
    # if a hang up occurs, it's probably not open, so we skip the port
    except:
        pass

def thread():
    while True:
        thread = queue.get()
        portscan(thread)
        queue.task_done()

queue = Queue()
start_time = time.time()

for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

for thread in range(1, 500):
    queue.put(thread)

queue.join()
print('Time taken:', time.time() - start_time)