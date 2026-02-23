from Seq0 import seq_reverse, seq_read_fasta

file_path = "Sequences/U5.fa"
sequence = seq_read_fasta(file_path)
fragment = sequence[:20]

print(f"Gene U5")
print(f"Fragment: {fragment}")

reverse_fragment = seq_reverse(fragment, 20)
print(f"Reverse: {reverse_fragment}")
