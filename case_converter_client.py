from socket import *

server = input('Server ip (default localhost): ') or 'localhost'  
port = 9999
keep = 1

conn_type = int(input('Connection type:\n0 - TCP (default)\n1 - UDP\n-> ') or 0) #0: TCP, 1: UDP
if conn_type == 0:
   with socket(AF_INET,SOCK_STREAM)	as client: # creates an tcp socket (client side)
    client.connect((server,port))

    while keep != 0:
        txt = input('Enter your sentence: ')
        to = int(input('Convertion type:\nTo lower: 0\nTo upper (default): 1\n-> ') or 1)

        msg = '1;' + txt if to else '0;' + txt

        enc_msg = msg.encode()
        client.send(enc_msg) 

        mod_msg = client.recv(1500)         
        dec_msg = mod_msg.decode()

        print('-'*5+f'\n{dec_msg}\n'+'-'*5)   # print received/decoded message

        keep = 0 if input('\nWant to enter another sentence?\nYes: Any key, No: 0\n-> ') == '0' else 1


elif conn_type == 1:
    clientSocket = socket(AF_INET, SOCK_DGRAM)  # creates a socket (client side)

    txt = input('Enter your sentence: ')
    to = int(input('Convertion type:\nTo lower: 0\nTo upper (default): 1\n-> ') or 1)

    msg = '1;' + txt if to else '0;' + txt

    encodedMessage = msg.encode()
    clientSocket.sendto(encodedMessage, (server, port))     # sends the message to server (no need to use connect() before, since it is UDP)

    modifiedMessage, serverIP = clientSocket.recvfrom(1500)         # 1500 bytes are read from the UDP socket
    decodedMessage = modifiedMessage.decode()

    print(decodedMessage)   # print received/decoded message

    clientSocket.close()