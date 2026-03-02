from Seq1 import Seq
from pathlib import Path

U5 = "../P00_PABLO_CACERES/Sequences/U5.fa"
ADA = "../P00_PABLO_CACERES/Sequences/ADA.fa"
FRAT1 = "../P00_PABLO_CACERES/Sequences/FRAT1.fa"
FXN = "../P00_PABLO_CACERES/Sequences/FXN.fa"
RNU6_269P = "../P00_PABLO_CACERES/Sequences/RNU6_269P.fa"

# Gene 1
s1 = Seq()
s11 = s1.read_fasta(U5)
seq1 = Seq(s11)

# Gene 2
s2 = Seq()
s22 = s2.read_fasta(ADA)
seq2 = Seq(s22)

# Gene 3
s3 = Seq()
s33 = s3.read_fasta(FRAT1)
seq3 = Seq(s33)

# Gene 4
s4 = Seq()
s44 = s4.read_fasta(FXN)
seq4 = Seq(s44)

# Gene 5
s5 = Seq()
s55 = s5.read_fasta(RNU6_269P)
seq5 = Seq(s55)

print(f"GENE 1: U5 Most frequent base: {seq1.frequency()}")
print()

print(f"GENE 2: ADA Most frequent base: {seq2.frequency()}")
print()

print(f"GENE 3: FRAT1 Most frequent base: {seq3.frequency()}")
print()

print(f"GENE 4: FXN Most frequent base: {seq4.frequency()}")
print()

print(f"GENE 5: RNU6_269P Most frequent base: {seq5.frequency()}")
print()
