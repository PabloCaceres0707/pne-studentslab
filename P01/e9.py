from Seq1 import Seq

s = Seq()

s.read_fasta("../P00_PABLO_CACERES/Sequences/U5.fa")

print(f"\nSequence 1: (Length: {s.len()}) {s}")
print("\nBases:" , s.count())
print("\nRev:", s.reverse())
print("\nComp:", s.seq_complement())