# import required modules

import socket
import threading

HOST = '127.0.0.1'
PORT = 8081
LISTENER_LIMIT = 5


def main():
    # creating the socket class object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # creating a try catch block

    try:
        server.bind((HOST, PORT))

    except Exception as e:
        print('unable to bind')

    # set server limit

    server.listen(LISTENER_LIMIT)

    # while loop keep listening to client connections

    while True:
        client, address = server.accept()
        print('successfully connected')


if __name__ == '__main__':
    main()
