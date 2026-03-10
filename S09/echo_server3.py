import socket


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "212.128.255.96"

ls.bind((IP, PORT))

ls.listen()


connection_count = 0
client_list = []

print(f"The server is configured on {IP}:{PORT}")

while True:
    print("\nWaiting for Clients to connect...")

    try:
        (cs, client_ip_port) = ls.accept()



    except KeyboardInterrupt:
        print("\nServer stopped by the user")
        ls.close()
        exit()

    else:
        connection_count += 1
        client_list.append((cs, client_ip_port))
        client_ip = client_ip_port[0]
        client_port = client_ip_port[1]

        print(f"Connection nr: {connection_count}")
        print(f"Client IP: {client_ip}")
        print(f"Client Port: {client_port}")


        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Message received: {msg}")

        cs.send(msg.encode())

        cs.close()


        if connection_count == 5:
            for i in range(len(client_list)):
                client = client_list[i]
                print(f"Client {i + 1}: IP = {client[0]}, Port = {client[1]}")

            ls.close()
            print("FINISHED")
            exit()
