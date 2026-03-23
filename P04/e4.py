import socket
import termcolor


# He configurado los parámetros de red del servidor
IP = "127.0.0.1"
PORT = 8080
PATH = "./P04/"

def process_client(s):
    # Teacher, recibo el mensaje de solicitud del cliente
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # Teacher, divido el mensaje en líneas
    lines = req.split('\n')

    # Teacher, la primera línea es la solicitud
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # He preparado el cuerpo de la respuesta
    try:
        file = PATH + "html" + str(req_line).split(" ")[1] + ".html"
        content = open(file)
        body = content.read()
        content.close()
    except FileNotFoundError:
        body = ""

    print("body = " + body)


    # He respondido con código 200 OK
    status_line = "HTTP/1.1 200 OK\n"

    # Añado el encabezado Content-Type
    header = "Content-Type: text/html\n"

    # Incluyo el encabezado Content-Length
    header += f"Content-Length: {len(body)} \n"

    # He creado el mensaje de respuesta
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# Teacher, ahora configuro el servidor
# Creo el socket de escucha
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Evito que el puerto esté en uso
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configuro IP y puerto
ls.bind((IP, PORT))

# El socket escucha conexiones entrantes
ls.listen()

print("Server configured!")

# Teacher, aquí comienza el bucle principal
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Atiendo al cliente
        process_client(cs)

        # Cierro el socket
        cs.close()