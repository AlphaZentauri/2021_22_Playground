from dataclasses import dataclass

@datclass
class PersonDataClass:
    firstname: str
    lastname: str
    birthdate: str

p = PersonDataClass("Egon", "Koch", "06.09.2004")
n = PersonDataClass("Jamie", "Holzer", "27.06.2005")
print(p,n)

