from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Telebe elave olundu: {student.name}")

    def remove_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print(f"Telebe silindi: {name}")
                return
        print(f"Telebe tapilmadi: {name}")

    def list_students(self):
        if not self.students:
            print("Bele telebe yoxdur")
        for s in self.students:
            print(s)

    def list_faculties(self):
        faculties = {s.faculty for s in self.students}
        if faculties:
            print("Fakulteler:")
            for f in faculties:
                print(f"- {f}")
        else:
            print("Fakulte yoxdur")

    def save_to_file(self, filename="students.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for s in self.students:
                birth_str = f"{s.birthdate[0]}/{s.birthdate[1]}/{s.birthdate[2]}"
                line = f"{s.name},{s.age},{s.faculty},{birth_str}\n"
                f.write(line)
        print(f"Telebeler '{filename}' faylina yazildi")
