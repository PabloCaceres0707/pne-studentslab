student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}


print(student["name"])
print(len(student["subjects"]))

if "PNE" in student["subjects"]:
    print("True")
else:
    print("False")

print(student["grades"]["Databases"])


average = ((student["grades"]["Networks"] + student["grades"]["PNE"] + student["grades"]["Databases"]) / 3)
print("Average Grade Between subjects", round(average, 2))

for clave, valor in student["grades"].items():
    print(clave, valor)