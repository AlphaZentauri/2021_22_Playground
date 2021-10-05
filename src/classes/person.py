from dataclasses import dataclass

@dataclass
class PersonDataClass:
    firstname: str
    lastname: str
    birthdate: str

p = PersonDataClass("Egon", "Koch", "06.09.2004")
print(p)
