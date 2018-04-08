from socket import *
host = "192.168.137.184"
print host
port = 6000
s = socket(AF_INET,SOCK_STREAM)
print "Socket Made"
s.bind((host,port))
print "Socket bound"
s.listen(5)
print "Listening"
q,addr = s.accept()
q.send("TEST")
s.close()
print("Done")
