import http.client
import json

# Server and endpoint (Estos son los que habeis puesto en lawiki profe)
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

URL = ENDPOINT + PARAMS

# Información básica para poner exactamente lo que aparece abajo al printear
print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{URL}")

# LO más importante crear la conexion
conn = http.client.HTTPConnection(SERVER)

# Send GET request
conn.request("GET", URL)

# Get response
rpablo = conn.getresponse()
print(f"Response received: {rpablo.status} {rpablo.reason}")

# Read and decode JSON data
data = rpablo.read().decode("utf-8")
response = json.loads(data)

# miro el ping
if response.get("ping") == 1:
    print("\nPING OK! The database is running!")
else:
    print("\nERROR: The database is not responding correctly")

# Y cierro
conn.close()