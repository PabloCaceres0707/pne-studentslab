dna_chain = input("Introduce the DNA sequence: ")

def counting_bases(sequence):
    a = 0
    c = 0
    g = 0
    t = 0
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            a += 1
        elif sequence[i] == "C":
            c += 1
        elif sequence[i] == "G":
            g += 1
        elif sequence[i] == "T":
            t += 1
    total_chain = a + c + g + t
    return total_chain, a, c, g, t

total_chain, a, c, g, t = counting_bases(dna_chain)

print("Total Length:", total_chain)
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)