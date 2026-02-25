from Seq1 import Seq

s = Seq()

s.read_fasta("../P00_PABLO_CACERES/Sequences/U5.fa")

print(f"Sequence 1: (Length: {s.len()}) {s}")
print("Bases:" , s.count())
print("Rev:", s.reverse())
print("Comp:", s.seq_complement())