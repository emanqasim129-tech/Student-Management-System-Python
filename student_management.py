students=[]
def add_student(students):
    print()
    name=input("Name:")

    while True:
        try:
            age=int(input("Age:"))
            break
        except ValueError:
            print("InValid Age! Try Again")

    while True:
        try:
            marks=int(input("Marks:"))
            if marks<0 or marks>100:
                print("Marks must be between 0 and 100")
                continue
            break
        except ValueError:
            print("Invalid Marks! Enter a valid marks.")
    student={
        "name":name,
        "age":age,
        "marks":marks
        }
    students.append(student)
    save_student(student)
    print()

def save_student(student):
    with open("StudentInfo.txt","a") as file:
        file.write(f"{student['name']}, {student['age']}, {student['marks']}\n")


def view_student(students):
    print()

    for student in students:
        print("Name: ",student["name"])
        print("Age: ",student["age"])
        print("Marks: ",student["marks"])
        print()

def load_student():
    students=[]
    try:
        with open("StudentInfo.txt","r") as file:
            for line in file:
                name, age, marks=line.strip().split(",") 
                student={
                    "name":name,
                    "age":int(age),
                    "marks":int(marks)
                }
                students.append(student)
    except FileNotFoundError:
        pass
    return students

def search_student(students):
    found=False
    name=input("Enter student name: ")
    for student in students:
        if student["name"].lower() ==name.lower():
            found=True
            print("\nStudent Found!\n")
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Marks: ",student["marks"])
            print()
            break
    if not found:
        print("Student not found.")

def grade(marks):
    if marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=50:
        return "D"
    else:
        return "F"
    
def is_pass(marks):
    return marks>=50

def student_Result(students):
    print()
    name=input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            marks=student["marks"]
            print("Marks: ", marks)
            print("Grade: ", grade(marks))
            if is_pass(marks):
                print("Status: Pass")
            else:
                print("Status: Fail")
            print()
            break
    else:
        print("Student not found.")


def main():
    print("\n____Student Management System____\n")
    students=load_student()
    while True:
        print()
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Student Result")
        print("5. Exit\n")
        try:
            choice=int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid Choice. Enter a number.")
            continue
        
        if choice==1:
            add_student(students)
        elif choice==2:
            view_student(students)
        elif choice==3:
            search_student(students)
        elif choice==4:
            student_Result(students)
        elif choice==5:
            print("--Exit--")
            break
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()