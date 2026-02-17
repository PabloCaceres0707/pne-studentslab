from pathlib import Path


FILENAME = "Sequences/RNU6_269P.fa"


file_contents = Path(FILENAME).read_text()


print(file_contents)
