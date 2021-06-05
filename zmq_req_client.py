import zmq
import sys

context = zmq.Context()
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello")
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request,message))

socket.close()

'''
for request in range(10):
    try:
        print("Sending request %s ..." % request)
        socket.send(b"Hello")
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request,message))
    except:
        print("exception exit.")
    finally:
        socket.close()
        sys.exit()
'''

