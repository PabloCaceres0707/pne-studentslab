from Client0 import Client
from Seq1 import Seq

# Teacher esta es mi Configuración Personalizada ---
RUTA_GEN = "../Sequences/FRAT1.txt"
manejador_seq = Seq()


HOST_IP = "212.128.255.94"
PTO_A = 8080
PTO_B = 8081

#Aquí creo dos instalaciones
enlace_uno = Client(HOST_IP, PTO_A)
enlace_dos = Client(HOST_IP, PTO_B)


def segmentar_cadena(texto_adn):

    lista_trozos = []

    for i in range(10):
        inicio = i * 10
        fin = inicio + 10
        trozo = texto_adn[inicio:fin]
        lista_trozos.append(trozo)
    return lista_trozos


# Teacher ejecuto bien el programa
print(">>> Iniciando Protocolo de Envío Fragmentado <<<")
print(f"Destino A: {enlace_uno}")
print(f"Destino B: {enlace_dos}")

# Cargo los datos desde el FASTA, esto dijisteis que era imprescindible en clase
adn_completo = manejador_seq.seq_read_fasta(RUTA_GEN)
print(f"\nSecuencia cargada (FRAT1): {adn_completo}")


bloques = segmentar_cadena(adn_completo)

print("\nTransfiriendo paquetes...")


for idx, contenido in enumerate(bloques, start=1):
    print(f"Paquete #{idx}: {contenido}")


    if idx % 2 != 0:
        print(f"  [Canal 1 - Puerto {PTO_A}] Enviando...")
        respuesta = enlace_uno.talk(contenido)
    else:
        print(f"  [Canal 2 - Puerto {PTO_B}] Enviando...")
        respuesta = enlace_dos.talk(contenido)

    print(f"  Respuesta recibida: {respuesta.strip()}")

print("\n--- Tarea finalizada con éxito ---")