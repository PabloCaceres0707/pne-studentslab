file = "Sequences/U5.fa"


from Seq0 import seq_read_fasta

print("The filename is: ", file,"\nThe first 20 bases are:", seq_read_fasta(file)[0: 20])

