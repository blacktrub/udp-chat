import socket
import threading
import os


UDP_MAX_SIZE = 65535


def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('ascii') + '\n' + f'you: ', end='')


def connect(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    s.send('__join'.encode('ascii'))

    while True:
        msg = input(f'you: ')
        s.send(msg.encode('ascii'))


if __name__ == '__main__':
    os.system('clear')
    print('Welcome to chat!')
    connect()

