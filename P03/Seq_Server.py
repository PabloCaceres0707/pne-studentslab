import socket
from Seq1 import Seq

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

sequences = [
    "ACCTCTCCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAATTTTCCCCGGGGAAAATTTTCCCCGGGGAAAATTTTCCCCGGGGAAAATTTTCCCC",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "GGGGCCCCAAAATTTTGGGGCCCCAAAATTTTGGGGCCCCAAAATTTTGGGGCCCCAAAA"
]


print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")
#----------------------------------------------------EXERCISE 1--------------------------------------------------------
        if msg == "PING":
            print("PING command!")
            response = "OK!\n"
# ----------------------------------------------------EXERCISE 2--------------------------------------------------------
        elif msg[0:3] == "GET":
            try:
                num_str = msg[4:].strip()
                index = int(num_str)

                if 0 <= index < len(sequences):
                    response = sequences[index] + "\n"
                else:
                    response = "ERROR: Index out of range\n"
            except:
                response = "ERROR: Invalid GET format\n"
# ----------------------------------------------------EXERCISE 3--------------------------------------------------------
        elif msg.startswith("INFO"):
            sc = Seq(msg.split(" ")[1])
            response = (f"Sequence: {sc}\n"
                        f"Length: {len(sc)}\n"
                        f"{sc.count()}")
# ----------------------------------------------------EXERCISE 3--------------------------------------------------------
        elif msg.startswith("COMP"):
            sq = Seq(msg.split(" ")[1])
            response






        cs.close()
