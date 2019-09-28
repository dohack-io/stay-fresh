    # -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:58:41 2019

@author: Benjamin Weber
"""
# server_neonious.py

def parsePacket(input_string):  

    if input_string == 'Hello':
        res = 0
    else:
        res = -1
    return res

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):

    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)


    import sys
    siz = sys.getsizeof(input_from_client_bytes)
    if  siz >= MAX_BUFFER_SIZE:
        print("Packet size is to large: {}".format(siz))

    # decode and parse packet from neonious
    input_from_client = input_from_client_bytes.decode("utf8").rstrip()
    print("Packet content: {}".format(input_from_client))
    res = parsePacket(input_from_client)
    
    if res == 0:
        print("packet valid!")
    else:
        print("invalid packet!")

    conn.close()
    print('Connection ' + ip + ':' + port + " ended")

def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("192.168.0.100", 12345))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #start listening
    soc.listen(10)
    print('Socket now listening')

    # thread handling for multiple connections
    from threading import Thread

    # client loop
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('New connection: ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Error while creating thread!")
            import traceback
            traceback.print_exc()
    soc.close()

start_server()  