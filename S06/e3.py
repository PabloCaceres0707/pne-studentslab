
class Seq:

    def __init__(self, strbases):
        valid_bases = "ACGT"

        for base in strbases:
            if base not in valid_bases:
                self.strbases = "ERROR"
                print("ERROR")
                return

        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases


    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    i = 0
    while i < len(seq_list):
        print(f" Sequence {i}: (Length: {seq_list[i].len()}) {seq_list[i]}")
        i += 1


def generate_seqs(pattern, number):
    i = 1
    seq_list = []
    while i <= number:
        seq_list.append(Seq(pattern * i))
        i += 1
    return seq_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print("List 2:")
print_seqs(seq_list2)

