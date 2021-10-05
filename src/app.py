from dataclasses import dataclass

@datclass
class PersonDataClass:
    firstname: str
    lastname: str
    birthdate: str

p = PersonDataClass("Egon", "Koch", "06.09.2004")
n = PersonDataClass("Jamie", "Holzer", "27.06.2005")

persons = [p, n]
for personen in persons:
    print(personen)

def printPersonen(persons):
    persons = [p, n]
    for personen in persons:
        print(personen)
    if name == main:
        printPersons(persons)

