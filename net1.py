import socket

#ip = socket.gethostbyname("www.google.com")
#print(ip)
#host = socket.gethostbyaddr(str(ip))
#print(host)

#port = socket.getservbyname('telnet')
#print(port)

#service_name = socket.getservbyport()
#print(service_name)

#                   IPv4            #UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#          #IP       #port
s.bind(("127.1.2.1",2223))
#recever data from client
Rdata , adress = s.recvfrom(1024)
#decode data from client
data=Rdata.decode('UTF-8')
data_for_send = "my response"

#encoder data for send
Sdata = data_for_send.encode("UTF-8")
#send Sdata to client adress
s.sendto(Sdata,adress)

print("data recieved from {} : \n {} ".format(adress,data))
