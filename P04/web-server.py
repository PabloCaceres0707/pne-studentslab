# PROFES, HE HECHO ESTE WEB SERVER, ESTE CODIGO ES UN PEQUEÑO SERVIDOR HTTP QUE ENTREGA PÁGINAS HTML SEGÚN LA RUTA Y ESPERO QUE OS GUSTE.
# AHORA, PUEDES VER QUE EL SERVIDOR SE HA CONSTRUIDO DE MANERA SIMPLE PERO EFICIENTE PARA GESTIONAR LAS PETICIONES
#ME FUNCIONA PERFECTO, SI HAY ALGUN PROBLEMA , ME DECIS, UN SALUDO.

import socket
import termcolor
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]
    parts = req_line.split(" ")
    path = parts[1]
    path_list = ["/info/A", "/info/G", "/info/C", "/info/T", "/"]

    if path in path_list:
        body = Path(f"html{path}.html").read_text() if path != "/" else Path("html/index.html").read_text()
    else:
        body = Path("html/Error.html").read_text()

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    s.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("DNA server configured")

while True:
    print("Esperando a los clientes....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()