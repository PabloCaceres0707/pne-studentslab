from Seq0 import most_frequent_base, seq_read_fasta

files = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 8 |------")

for gene in files:
    sequence = seq_read_fasta(f"Sequences/{gene}.fa")
    base = most_frequent_base(sequence)
    print(f"Gene {gene}: Most frequent Base: {base}")