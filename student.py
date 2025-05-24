class Student:
    def __init__(self, name, age, faculty, birthdate):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.birthdate = birthdate 

    def __str__(self):
        return f"{self.name}, {self.age} yas, Fakulte: {self.faculty}, Dogum tarixi: {self.birthdate[0]}/{self.birthdate[1]}/{self.birthdate[2]}"
