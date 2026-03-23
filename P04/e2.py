import socket
import termcolor

# He configurado los parámetros de red del servidor
IP = "127.0.0.1" #OBVIAMENTE LA IP QUE NOS AHABEIS DADO
PORT = 8080
PATH = "./P04/"


def process_client(s):
    # Teacher, lo primero que hago es recibir el mensaje de la solicitud del cliente
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # Divido el mensaje de la solicitud en líneas
    lines = req.split('\n')

    # La primera línea es la solicitud
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # Ahora genero el mensaje de respuesta
    # Incluye la línea de estado, los encabezados, una línea en blanco y el cuerpo

    # Aquí preparo el cuerpo de la respuesta

    try:
        file = PATH + "html" + str(req_line).split(" ")[1] + ".html"
        content = open(file)
        body = content.read()
        content.close()
    except FileNotFoundError:
        body = ""

    print("body = " + body)

    # En la línea de estado, respondo que esta guay/bien
    status_line = "HTTP/1.1 200 OK\n"

    # Añado el encabezado Content-Type
    header = "Content-Type: text/html\n"

    # Incluyo también el encabezado Content-Length
    header += f"Content-Length: {len(body)} \n"

    # Finalmente, construyo el mensaje de respuesta uniendo todas las partes
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# Teacher, paso a configurar el servidor
# Configuración del servidor
# Creo el socket de escucha
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establezco una opción para evitar que el puerto ya esté en uso
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Establezco la IP y el puerto del socket
ls.bind((IP, PORT))

# Hago que el socket se convierta en un socket de escucha
ls.listen()

print("Server configured!")

# Teacher, a continuación inicio el bucle principal del servidor
# Bucle principal
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

        # Después de atender al cliente, cierro el socket
        cs.close()