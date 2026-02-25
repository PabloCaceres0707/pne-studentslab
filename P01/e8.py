from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print("Bases:" , s1.count())
print("Rev:", s1.reverse())
print("Comp:", s2.seq_complement())

print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print("Bases:" , s2.count())
print("Rev:", s2.reverse())
print("Comp:", s2.seq_complement())

print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print("Bases:" , s3.count())
print("Rev:", s3.reverse())
print("Comp:", s2.seq_complement())