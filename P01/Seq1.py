
from pathlib import Path

class Seq:

    def __init__(self, strbases=None):
        valid_bases = "ACGT"

        if not strbases:
            self.strbases = "NULL"
            print("NULL sequence created! ")
            return

        for base in strbases:
            if base not in valid_bases:
                self.strbases = "ERROR"
                print("Invalid sequence!")
                return

        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases


    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)


    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0

        return self.strbases.count(base)


    def count(self):
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        if self.strbases == "NULL" or self.strbases == "ERROR":
            return counts

        for base in self.strbases:
            if base in counts:
                counts[base] += 1

        return counts

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            seq_reversed = self.strbases[::-1]
            return seq_reversed

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases

        complement_map = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
        sequence_c = ""

        for base in self.strbases:
            if base in complement_map:
                sequence_c += complement_map[base]
            else:
                sequence_c += base

        return sequence_c

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        file_contents = file_contents.split("\n")
        body = "\n".join(file_contents[1:])
        self.strbases = body
        return self.strbases