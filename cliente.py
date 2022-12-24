# import required modules
import socket
import threading


HOST = '127.0.0.1'
PORT = 8081


def main():
    # creating the socket class object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST, PORT))
    except:
        print('Connection failed')


if __name__ == '__main__':
    main()
