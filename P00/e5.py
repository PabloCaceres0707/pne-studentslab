from Seq0 import seq_count, seq_count_print

FOLDER = "Sequences/"

sequence = ["Sequences/U5.fa", "Sequences/ADA.fa", "Sequences/FXN.fa", "Sequences/FRAT1.fa"]

bases = ["A", "C", "G", "T"]

seq_count_print(sequence,bases)
print("\n", seq_count(sequence,bases))


