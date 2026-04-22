import http.client
import json

# The dictionary of genes
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

server = "rest.ensembl.org"



# ESTE ES EL LOOP MÁS IMPORTANTE, QUE ES EL QUE TE SIRVE PARA IR ITERAND
for gene_name, gene_id in genes.items():
    endpoint = f"/sequence/id/{gene_id}?content-type=application/json"

    connection = http.client.HTTPConnection(server)
    connection.request("GET", endpoint)
    response = connection.getresponse()

    if response.status == 200:
        data = json.loads(response.read().decode('utf-8'))
        seq = data['seq']




        # AQUÍ SIRVE PARA HACER LOS calsculos
        total_len = len(seq)
        counts = {'A': seq.count('A'), 'C': seq.count('C'),
                  'G': seq.count('G'), 'T': seq.count('T')}
        most_frequent = max(counts, key=counts.get)

        # AQUI SON LOS RESULTADOS DE CADA GEN , QUE SE VA A VER
        print(f"--- Processing {gene_name} ---")
        print(f"Gene: {gene_name}")
        print(f"Description: {data['desc']}")
        print(f"Total length: {total_len}")
        for base, count in counts.items():
            percentage = (count / total_len) * 100
            print(f"{base}: {count} ({percentage:.1f}%)")
        print(f"Most frequent Base: {most_frequent}\n")

    connection.close()