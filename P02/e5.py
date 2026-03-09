from Client0 import Client
from Seq1 import Seq

#COSAS IMPORTANTE TEACHER: a la hora de :from Seq1 import Seq , a mi me va bien pero no estoy seguro si desde vuestro ordenador es igual
#SEGUNDO COSA IMP: la ruta para encontrar FRAT1 ME VA A MI DESDE AQUI CON LO QUE HE PUESTO, pero repito no se si a vosotros os va desde vuestro ordenador.
#A mi en principio me va absolutamente todosi teneis algún problema me comentais


FRAT1 = "..../P00_PABLO_CACERES/Sequences/FRAT1.fa"
s = Seq()
IP = "212.128.255.94"
PORT = 8080

def cut(string):
    fragments = []
    for i in range(5):
        start_index = i * 10
        end_index = start_index + 10
        fragments.append(string[start_index:end_index])
    return fragments

c = Client(IP, PORT)
sequence = s.read_fasta(FRAT1)
fragments = cut(sequence)

print(f"Gene FRAT1: {sequence}")
for i, ch in enumerate(fragments, 1):
    print(f"Fragment {i}: ")
    response = c.talk(ch)
    print(f"Response: {response}")