from base64 import decode
from socket import *

host = input('Host IP (default localhost): ') or 'localhost'
port = 9999	


conn_type = int(input('Connection type:\n0 - TCP (default)\n1 - UDP\n-> ') or 0) #0: TCP, 1: UDP

if conn_type == 0:
   with socket(AF_INET,SOCK_STREAM)	as server: # creates an tcp socket (server side)    
        server.bind((host,port))
        server.listen()
        print(f'Server is listening on {host}:{port} with TCP connection!')
        conn, addr = server.accept()
        
        with conn:
            print(f'Connection succesfull with client {addr}')
            while 1:
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
    print(f'Server is listening on port {port} with UDP connection!')

    while 1:
        message, clientIP = server.recvfrom(1500)		# 1500 bytes are read from the UDP socket
        decodedMessage = message.decode()
        print(f'Received message: {message}, Decoded messsage: {decodedMessage}')

        modifiedMessage = decodedMessage.upper()
        encodedMessage = modifiedMessage.encode()
        print(f'Modified message: {modifiedMessage}, Encoded messsage: {encodedMessage}')

        server.sendto(encodedMessage, clientIP)		# sends converted (upper-case) sentence