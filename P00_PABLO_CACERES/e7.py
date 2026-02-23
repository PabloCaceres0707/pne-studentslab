from Seq0 import seq_complement, seq_read_fasta

file_path = "Sequences/U5.fa"
sequence = seq_read_fasta(file_path)
fragment = sequence[:20]

print(f"-----| Exercise 7 |------")
print(f"Gene U5:")
print(f"Frag: {fragment}")

complement_fragment = seq_complement(fragment, 20)
print(f"Comp: {complement_fragment}")