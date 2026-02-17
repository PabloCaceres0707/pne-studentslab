
from pathlib import Path


FILENAME = "Sequences/ADA.fa"


file_contents = Path(FILENAME).read_text().splitlines()

body = "".join(file_contents[1:]).strip()
sequence = len(body)
print("Total number of Bases:", sequence)