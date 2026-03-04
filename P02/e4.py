from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.94"
PORT = 8080

c = Client(IP, PORT)
print(c)

genes_info = {
    "U5": "../P00_PABLO_CACERES/Sequences/U5.fa",
    "FRAT1": "../P00_PABLO_CACERES/Sequences/FRAT1.fa",
    "ADA": "../P00_PABLO_CACERES/Sequences/ADA.fa"
}

for gene_name, file_path in genes_info.items():

    s = Seq()
    s.read_fasta(file_path)


    msg_info = f"Sending {gene_name} Gene to the server..."
    print(f"To Server: {msg_info}")
    response = c.talk(msg_info)
    print(f"From Server:\n{response}\n")


    gene_seq = str(s)
    print(f"To Server: {gene_seq}")
    response = c.talk(gene_seq)
    print(f"From Server:\n{response}\n")