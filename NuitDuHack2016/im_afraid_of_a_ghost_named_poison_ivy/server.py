#!/usr/bin/env python

import socket
import camellia
import zlib
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE =1024

#cle
key="casper"
key=key[:32]
key=key+"\x00"*(32-len(key))


#connection init
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#recup connection
conn, addr = s.accept()
#print 'Connection address:', addr
data = conn.recv(BUFFER_SIZE)
#header=data[:5]
#print 'header: ',header
#k=struct.unpack("<L", data[5:9])[0]
#print 'len_packet: ',k
#j=struct.unpack("<L", data[9:13])[0]
#print 'len_uncomp: ' ,j
#print "received data:", (data[15:]).encode('hex')
#print zlib.decompress(data[15:])

#reponse
chall=zlib.decompress(data[13:])
chall+="\x00"*(128-len(chall))
c=camellia.CamelliaCipher(key=key,mode=camellia.MODE_ECB)
chall_enc=c.encrypt(chall)
print len(zlib.compress(chall_enc))
MESSAGE="gh0st"+"\x9A\x00\x00\x00"+"\x80\x00\x00\x00"+zlib.compress(chall_enc)
conn.send(MESSAGE)  # echo

#send payload,flag
flag="flag_seriously_wtf_is_that?"
flag+="\x00"*(32-len(flag))
flag_enc=c.encrypt(flag)
print 'len data',len(zlib.compress("\x20\x00\x00\x00"+flag_enc))
print 'len flag_enc',len(flag_enc)

print ("\x20\x00\x00\x00"+flag_enc).encode('hex')

MESSAGE2="gh0st"+"\x3c\x00\x00\x00"+"\x24\x00\x00\x00"+zlib.compress("\x20\x00\x00\x00"+flag_enc)
conn.send(MESSAGE2)  # echo
print 'len msg',len(MESSAGE2)



conn.close()
                    
