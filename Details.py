# def load_students():
#     students = []

#     with open("student_details.txt","r") as f:
#         for line in f:
#             sID,name,marks = line.strip().split(',')
#             students.append({"id": sID, "name": name, "marks": marks})
#     return students


# students = load_students()
def load_students():
    students = []
    try:
        with open("student_details.txt","r") as f:
            for line in f:
                sID, name, marks = line.strip().split(',')
                students.append({"id": sID, "name": name, "marks": marks})
    except FileNotFoundError:
        pass  # if file doesn't exist, start with an empty list
    return students


students = load_students()

def add_student():
    sid = input("Enter student ID :")
    sname = input("Enter student name :")
    smarks = input("Enter student marks :")

    student = {"id":sid,"name":sname,"marks":smarks}

    students.append(student)

    print("Student added sucessfully ! \n")


def view_student():
    # print("DEBUG: ", students)
    if len(students) == 0:
        print("Student not found")
    else:
        print("\n --- students list ---")
        for s in students:
           print(f"ID : {s['id']}, Name : {s['name']}, Marks : {s['marks']}")
        print()
def search_student():
     number = input("Enter student ID to search :")
     found = False
     for s in students:
        if(s['id'] == number):
            print(f"ID : {s['id']}, Name : {s['name']}, Marks : {s['marks']}","\n")
            print()
            found = True
            break
        else:
            print("Student not found with the ID :",number,"\n")
def update_student():
    sID = input("Enter student ID to update :")
    found = False

    for s in students:
        if(s['id'] == sID):
            print("Current Details: \n")
            print(f"ID : {s['id']}, Name : {s['name']}, Marks : {s['marks']}","\n")

            new_name = input("Enter new name or (press enter to skip) :")
            new_marks = input("Enter new marks or (press enter to skip) :")

            if new_name.strip() != "":
                s['name'] = new_name
            if new_marks.strip() != "":
                s['marks'] = new_marks

            print("Student details updated sucessfully! \n")
            found = True
            break
    if not found:
        print("No student with ID",sID," found \n")
            

def delete_student():
    deleteID = input("Enter student id to delete :")
    found = False

    for s in students:
        if(s['id']==deleteID):
            students.remove(s)
            print("Student removed sucessfully.\n")

            found = True
            break

    if not found:
        print("Student id not found.\n")

def save_students(students):
    with open("student_details.txt","w") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['marks']} \n")


while True:
    choice = input("""===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice: """)
    if(choice == '1'):
        add_student()
    elif(choice == '2'):
        view_student()
    elif(choice == "3"):
        search_student()    
    elif(choice == "4"):
        update_student()    
    elif(choice == "5"):
        delete_student()    
    elif(choice == "6"):
        save_students(students)
        print("Exiting the program....")
        break
    else:
        print("Invalid choice. Please choose a correct choice \n")    
    
save_students(students)