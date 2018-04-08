from socket import *
host = "192.168.137.1"
print host
port = 6000
s = socket(AF_INET,SOCK_STREAM)
print "Socket Made"
try:
	s.bind((host,port))
except:
	host = "192.168.137.35"
	s.bind((host,port))
print "Socket bound"
s.listen(5)
print "Listening"
q,addr = s.accept()
print "connected"
q.send("can you hear me???")
print "sent message"
print "awaiting reply..."
print(q.recv(1024)[0])
print "Message received, closing socket..."
s.close()
print("Done")
