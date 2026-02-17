
from pathlib import Path


FILENAME = "Sequences/RNU6_269P.fa"


file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")
print("The first line of the RNU6_269P.fa file:", file_contents[0])
