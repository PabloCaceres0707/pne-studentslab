import socket
import termcolor

# Este código configura un servidor que escucha peticiones HTTP, responde con archivos HTML según la solicitud del cliente, y maneja errores si no encuentra el archivo solicitado.
IP = "127.0.0.1"  #AQUI HE METIDO LA ip que nos disteis, si hay algun problema meted la vuestra y pùnto. A mi me va bien, no se si a vosotros también
PORT = 8080
PATH = "./P04/"


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    link = str(req_line).split(" ")[1]
    if link == "/":
        file = PATH + "html/index.html"
        content = open(file)
    else:
        try:
            file = PATH + "html" + str(req_line).split(" ")[1] + ".html"
            content = open(file)

        except FileNotFoundError:
            file = PATH + "html/error.html"
            content = open(file)

    body = content.read()
    content.close()

    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)} \n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("Now it is configured!")

while True:
    print("Waiting for people....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()