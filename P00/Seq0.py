from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(file):
    file_contents = Path(file).read_text()
    file_contents = file_contents.split("\n")
    body = "\n".join(file_contents[1:])
    return body

def seq_len(sequence):
    for name in sequence:
        genes = seq_read_fasta(name)
        print("Gene Name:", name, "-->", len(genes))

def seq_count_base(files,bases):
    for names in files:
        genes = seq_read_fasta(names)
        print("Name:" + names)
        for gene in bases:
            print("Base:", gene, "-->", genes.count(gene))

#----------------------Exercise 5 ----------------------Con print y con return----------------#
def seq_count_print(files,bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(names)
        for gene in bases:
            dict[gene] = genes.count(gene)
        print("Gene", names, ":",dict)

def seq_count(files,bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(names)
        dict[names] = {}
        for gene in bases:
            dict[names][gene] = genes.count(gene)

    return dict