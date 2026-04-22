import http.client
import json

# DICCIONARIO DE LOS GENES
genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000207399",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226343",
    "RBMY2YP": "ENSG00000227159",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


# aqui lo utilizo el input para que me de el gen
gene_name = input("Write the gene name: ")


if gene_name in genes:
    gene_id = genes[gene_name]
    server = "rest.ensembl.org"
    endpoint = f"/sequence/id/{gene_id}?content-type=application/json"

    # 3. Esto lo he buscado apra que me quede perfecto, a mi asi me va.
    connection = http.client.HTTPConnection(server)
    connection.request("GET", endpoint)
    response = connection.getresponse()

    #Por ultimo el if imprescindible
    if response.status == 200:
        data = json.loads(response.read().decode('utf-8'))
        seq = data['seq']


        # 4. Process calculations
        total_len = len(seq)
        counts = {'A': seq.count('A'), 'C': seq.count('C'),
                  'G': seq.count('G'), 'T': seq.count('T')}


        # Determine most frequent base
        most_frequent = max(counts, key=counts.get)

        # 5. Aquí prineto los outputs

        print(f"Server: {server}")
        print(f"URL: {server}{endpoint}")
        print(f"Response received!: {response.status} {response.reason}")
        print(f"\nGene: {gene_name}")
        print(f"Description: {data['desc']}")
        print("New sequence created!")
        print(f"Total lengh: {total_len}")
        for base, count in counts.items():
            percentage = (count / total_len) * 100
            print(f"{base}: {count} ({percentage:.1f}%)")
        print(f"Most frequent Base: {most_frequent}")
    else:
        print("Error connecting to server.")
    connection.close()
else:
    print("Gene not found in dictionary.")