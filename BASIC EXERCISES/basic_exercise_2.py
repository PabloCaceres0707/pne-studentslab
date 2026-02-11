text = "  Hello, World! Welcome to Python Programming.  "

text_s = text.strip()
print("Stripped:", text_s)

text_1 = len(text.split())
print("Word Count:", text_1)

print("Uppercase:", text.title())

print("Starts with hello:", text_s.startswith("Hello"))
print("Ends with ing:", text_s.endswith("ing."))

print("Position Index:", text_s.find("Python"))

text_split = text.split()
print("Joined back:", " - ".join(text_split))