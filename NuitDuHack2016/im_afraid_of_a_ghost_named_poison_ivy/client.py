#!/usr/bin/env python

import socket
import random
import zlib
import camellia

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
Header = "gh0st"

#cle
key="casper"
key=key[:32]
key=key+"\x00"*(32-len(key))

chall=""
for i in xrange(0,100):
    chall+=chr(random.randrange(0,256))

c=camellia.CamelliaCipher(key=key,mode=camellia.MODE_ECB)

#connection init
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print " ".join(hex(ord(n)) for n in zlib.compress(chall))

#send chall
MESSAGE=Header+"\x7c\x00\x00\x00"+"\x64\x00\x00\x00"+zlib.compress(chall)
s.send(MESSAGE)

#reponse chall
data = s.recv(BUFFER_SIZE)
print "received data:", data
data2=zlib.decompress(data[13:])
chall_resp=c.decrypt(data2)
chall_resp=chall_resp[:len(chall)]
#print chall_resp.encode('hex')
if chall_resp==chall:
    print 'Good!'
else:
    print 'Bad'

data3 = s.recv(BUFFER_SIZE)
data4=zlib.decompress(data3[13:])
print data4.encode('hex')
resp=c.decrypt(data4[4:])
print resp




#end
s.close()



