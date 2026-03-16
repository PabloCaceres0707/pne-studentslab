
from Client0 import *


i = 0

while i < 6:

    IP = "127.0.0.1"   #HE HECHO LOS EJERCICIOS CON LA IP QUE PONIAIS Y ME HA IDO BIEN, SI HAY ALGÚN PROBLEMA PONED LA VUESTRA Y LISTO.
    PORT = 8080

    c = Client(IP, PORT)

    if i == 0:

        print("Sending a message to the server...")
        response = c.talk("PING")
        print(f"Response: {response}")


    if i == 1:

        print("Sending a message to the server...")

        print(c.talk("GET 0"))
        print(c.talk("GET 1"))
        print(c.talk("GET 2"))
        print(c.talk("GET 3"))
        print(c.talk("GET 4"))


    if i == 2:

        print("Sending a message to the server...")
        response = c.talk("INFO AAATTTGGGCCC")
        print(response)


    if i == 3:

        print("Sending a message to the server...")
        response = c.talk("COMP AAATTTGGGCCC")
        print(response)


    if i == 4:

        print("Sending a message to the server...")
        response = c.talk("REV AAATTTGGGCCC")
        print(response)


    if i == 5:

        print("Sending a message to the server...")

        print(c.talk("GENE U5"))
        print(c.talk("GENE ADA"))
        print(c.talk("GENE FRAT1"))
        print(c.talk("GENE FXN"))
        print(c.talk("GENE RNU6_269P"))


    i += 1