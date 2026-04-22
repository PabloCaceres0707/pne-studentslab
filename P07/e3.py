import http.client
import json

# SERVER y los ENDPOINTS

server = "rest.ensembl.org"
gene_id = "ENSG00000207552"  # Stable ID for MIR633
endpoint = f"/sequence/id/{gene_id}?content-type=application/json"

# AQUÍ ESTABLEZCO LA CONEXIÓN
connection = http.client.HTTPConnection(server)

# Enviar la GET REQUEST para que lo de
connection.request("GET", endpoint)

# Get the response
response = connection.getresponse()

# Mirar si ha sido exittosa la request (HTTP 200)
if response.status == 200:
    data = response.read().decode('utf-8')
    gene_data = json.loads(data)

    # Aquí lo más fácil, todos los prints
    print(f"Server: {server}")
    print(f"URL: {server}{endpoint}")
    print(f"Response received!: {response.status} {response.reason}")
    print(f"\nGene: MIR633")
    print(f"Description: {gene_data['desc']}")
    print(f"Bases: {gene_data['seq']}")
else:
    print(f"Error: {response.status} {response.reason}")

# CERRAR CONEXIÓN
connection.close()




