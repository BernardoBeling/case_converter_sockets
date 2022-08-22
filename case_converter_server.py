from base64 import decode
from socket import *

host = input('Host IP (default localhost): ') or 'localhost'
port = 9999	


conn_type = int(input('Connection type:\n0 - TCP (default)\n1 - UDP\n-> ') or 0) #0: TCP, 1: UDP

if conn_type == 0:
    server = socket(AF_INET,SOCK_STREAM) # creates an tcp socket (server side)    
    server.bind((host,port))
    server.listen()
    print(f'Server is listening on {host}:{port} with TCP connection!')
        
    while 1:
        conn, addr = server.accept()
        with conn:
            print(f'Connection succesfull with client {addr}')
            msg = conn.recv(1500)
            if not msg:
                break
            dec_msg = msg.decode()
            print(f'>Received message: {msg}\n>Decoded messsage: {dec_msg}')
            
            to, txt = dec_msg.split(';')

            new_txt = txt.upper() if int(to) else txt.lower() #0: to lower  1: to upper
            enc_msg = new_txt.encode()
            print(f'>Modified message: {new_txt}\n>Encoded messsage: {enc_msg}')

            conn.send(enc_msg)
else:
    server = socket(AF_INET,SOCK_DGRAM)	# creates an udp socket (server side)
    server.bind((host, port))	# bind() associates the socket with its local address [bind() is used in the server side]
    print(f'Server is listening on {host}:{port} with UDP connection!')

    while 1:
        message, clientIP = server.recvfrom(1500)		# 1500 bytes are read from the UDP socket
        print(f'Received from: {clientIP}')
        dec_msg = message.decode()
        print(f'Received message: {message}, Decoded messsage: {dec_msg}')

        to, txt = dec_msg.split(';')
        new_txt = txt.upper() if int(to) else txt.lower() #0: to lower  1: to upper
        enc_msg = new_txt.encode()

        print(f'Modified message: {new_txt}, Encoded messsage: {enc_msg}')

        server.sendto(enc_msg, clientIP)		# sends converted (upper-case) sentence