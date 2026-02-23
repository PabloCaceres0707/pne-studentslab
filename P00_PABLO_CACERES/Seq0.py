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


def seq_reverse(seq, n):
    seq_reversed = seq[0:n]
    return seq_reversed[::-1]

def seq_complement(sequence, n):
    sequence_new = sequence[0:n]
    sequence_c = ""

    for base in sequence_new:
        if base == 'T':
            sequence_c += "A"
        elif base == 'A':
            sequence_c += "T"
        elif base == 'G':
            sequence_c += "C"
        elif base == 'C':
            sequence_c += "G"
        else:
            sequence_c += base

    return sequence_c


def most_frequent_base(seq):
    bases = ["A", "T", "C", "G"]
    counts = {base: seq.count(base) for base in bases}
    return max(counts, key=counts.get)