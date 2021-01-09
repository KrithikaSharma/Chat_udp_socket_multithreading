import socket
import threading
import os

print("""
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			CHAT APPLICATION                 
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input("\nEnter your IP:")
port=int(input("Enter your port:"))
s.bind((ip,port))
s_ip=input("Enter server IP:")
s_port=int(input("Enter server port:"))


def recv():
	while True:
		x=s.recvfrom(1024)
		d=x[0].decode()
		o=os.popen("date +'%X' ").read()
		print("\t\t\t\t 15>> {} at {} ".format(d,o))
			
def send():
	while True:
		data=input("\nType a message:")
		data=str.encode(data)
		s.sendto(data,(s_ip,s_port))
	
		

t1=threading.Thread(target=recv)
t2=threading.Thread(target=send)
t1.start()
t2.start()
