from urwid import get_all_fonts


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


def count_bases_files(list):
    total_all = 0
    a_all = 0
    c_all = 0
    g_all = 0
    t_all = 0
    for seq in list:
        total, a,c,g,t = counting_bases(seq)
        total_all += total
        a_all += a
        c_all += c
        t_all += t
        g_all += g
    return total_all, a_all, c_all, g_all, t_all

txt_list = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
total, a, c, g, t = count_bases_files(txt_list)
print("Total length:", total)
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)


#-----------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Option 1

f = open("dna.txt", "r")

lines = f.readlines()
f.close()

#Option 2
with open("dna.txt", "r") as f:
    lines = f.readlines()

total_number = 0
bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for sequence in txt_list:
    sequence = sequence.strip()
    total_number += len(sequence)
    result = count_bases_files(sequence)

    for key in result:
        bases[key] += result[key]

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f'{base}: {count}')


