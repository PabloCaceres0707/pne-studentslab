

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



seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

def print_seqs(seq_list):
    i = 0
    while i < len(seq_list):
        print(f" Sequence {i}: (Length: {seq_list[i].len()}) {seq_list[i]}")
        i += 1

print_seqs(seq_list)

