import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data_for_send = "ma lettre"
Sdata = data_for_send.encode("UTF-8")
s.sendto(Sdata,("127.1.2.1",2223))
Rdata , adress = s.recvfrom(1024)
data = Rdata.decode("UTF-8")
print("data recieved from {} : \n {} ".format(adress,data))
