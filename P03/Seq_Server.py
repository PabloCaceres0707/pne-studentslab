#TEACHER A MI ME VE PERFECTO, Y HE UTILIZADO LA IP QUE HABEIS DADO EN LOS EJERCICIOS, HE ESTADO HACIENDO UNAS PRUEBAS, Y PESE A QUE
#ME VA PERFECTO ME TEMO QUE IGUAL AL HACERLO EN OTRO ORDENADOR LA IP SE PUEDE RALLAR AL NO SER EL LOCAHOST, LO QUE ES EL CÓDIGO
#EN PRINCIPIO ESTÁ BIEN, HE PROBADO TODOS LOS COMANDOS Y BIEN. SI HAY ALGUN PROBLEMA ME COMENTAIS, ESPERO QUE OS GUSTE
import socket

from P00_PABLO_CACERES.Seq0 import seq_complement
from Seq1 import *

PORT = 8080
IP = "127.0.0.1"

# Create socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Avoid port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
ls.bind((IP, PORT))

# Listen
ls.listen()

print("The server is configured!")

while True:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        x = msg.split(" ")

        if x[0] == "PING":
            print("PING Command!")
            response = "OK\n"

        if x[0] == "GET":

            if x[1] == "0":
                response = "AAAGGGTTTCCCAAAAA"

            if x[1] == "1":
                response = "AAAGGGTTTCCCAGGGG"

            if x[1] == "2":
                response = "AAAGGGTTTCCCAAGGG"

            if x[1] == "3":
                response = "AAAGGGTTTCCCAAAGG"

            if x[1] == "4":
                response = "AAAGGGTTTCCCAAAAG"


        if x[0] == "INFO":

            seq1 = x[1]

            s = Seq(seq1)

            dict_result = s.count_base()

            response = ""
            response += f"Sequence: {seq1}\n"
            response += f"Total length: {len(seq1)}\n"

            for base in ["A", "C", "G", "T"]:
                response += f"{base}: {dict_result[base]['times']} ({dict_result[base]['percentage']}%)\n"


        if x[0] == "COMP":

            seq1 = x[1]

            s = Seq(seq1)

            result = s.seq_complement()

            response = result


        if x[0] == "REV":

            seq1 = x[1]

            s = Seq(seq1)

            result = s.reverse()

            response = result

        if x[0] == "GENE":

            if x[1] == "U5":
                path = "../Sequences/U5.fa"

                s1 = Seq()

                response = s1.read_fasta(path)

            if x[1] == "ADA":
                path = "../Sequences/ADA.fa"

                s1 = Seq()

                response = s1.read_fasta(path)

            if x[1] == "FRAT1":
                path = "../Sequences/FRAT1.fa"

                s1 = Seq()

                response = s1.read_fasta(path)

            if x[1] == "FXN":
                path = "../Sequences/FXN.fa"

                s1 = Seq()

                response = s1.read_fasta(path)

            if x[1] == "RNU6_269P":
                path = "../Sequences/RNU6_269P.fa"

                s1 = Seq()

                response = s1.read_fasta(path)

        cs.send(response.encode())

        cs.close()