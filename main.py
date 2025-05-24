from student import Student
from student_manager import StudentManager
def input_birthdate():
    while True:
            day = int(input("Dogum gunu: "))
            month = int(input("Dogum ayi: "))
            year = int(input("Dogum ili: "))
            return (day, month, year)

def main():
    manager = StudentManager()

    while True:
        print("\n İdareetme Paneli")
        print("1. Telebe elave et")
        print("2. Telebeni sil")
        print("3. Siyahini goster")
        print("4. Fakulteleri goster")
        print("5. Fayla yaz")
        print("6. Cixis et")
        choice = input("Seciminizi daxil edin: ")

        if choice == "1":
            name = str(input("Ad: "))
            age = int(input("Yas: "))
            faculty = str(input("Fakulte: "))
            birthdate = input_birthdate()
            student = Student(name, age, faculty, birthdate)
            manager.add_student(student)

        elif choice == "2":
            name = input("Silinecek telebenin adi: ")
            manager.remove_student(name)

        elif choice == "3":
            manager.list_students()

        elif choice == "4":
            manager.list_faculties()

        elif choice == "5":
            manager.save_to_file()

        elif choice == '6':
            print("Cixilir...")
            break

        else:
            print("Yanlis secim")


if __name__ == "__main__":
    main()
