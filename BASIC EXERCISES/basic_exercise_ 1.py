dna = "ATGCGATCGATCGATCGATCGA"

print("length:", len(dna))
print("First 5:", dna[0: 5])
print("Last 3:", dna[-3:])
print("Lower case:", dna.lower())
print("ATC Count:", dna.count("ATC"))

def change_bases(sequence):
    new_sequence = ""
    for base in sequence:
        if base == "T":
            new_sequence += "U"
        else:
            new_sequence += base
    return new_sequence

print("New Base:", change_bases(dna))
