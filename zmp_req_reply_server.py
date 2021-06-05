

import time
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
receiveNum = 0
while True:
    print("wait message...")
    message = socket.recv()
    print("receive message : ", message)
    receiveNum = receiveNum + 1
    print("receive message number is: ", receiveNum)
    #do some work
    time.sleep(1)
    socket.send(b"World")
    print("send world.")
'''
while True:
    try:
        message = socket.recv()
        print("receive message %s "% message)
        #do some work
        time.sleep(1)
        socket.send(b"World")
        print("send world.")
        
    except Exception as e:
        print("exception: ",e)
        sys.exit()
        #socket.close()
'''
    


