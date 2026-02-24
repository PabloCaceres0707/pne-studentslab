

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


s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
s3 = Seq("AGHT")


print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Sequence 3: {s3}")
