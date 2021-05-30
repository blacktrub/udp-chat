import socket


UDP_MAX_SIZE = 65535


def listen(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))
    print(f'Listening at {host}:{port}')

    members = []
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)

        if addr not in members:
            members.append(addr)
        
        if not msg:
            continue

        client_id = addr[1]
        msg_text = msg.decode('ascii')
        if msg_text == '__join':
            print(f'Client {client_id} joined chat')
            continue

        message_template = '{}__{}'
        if msg_text == '__members':
            print(f'Client {client_id} requsted members')
            active_members = [f'client{m[1]}' for m in members if m != addr]
            members_msg = ';'.join(active_members)
            s.sendto(message_template.format('members', members_msg).encode('ascii'), addr)
            continue


if __name__ == '__main__':
    listen()
