students = []
print("="*45)
print("Welcome to Student Management System")
print("="*45)
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")
        student = {"Name": name, "Age": age, "Course": course}
        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
         if len(students) == 0:
              print("No students found!")
         else:
              print("\n----- Student List -----")
              for student in students:
                   print(f"Name: {student['Name']}")
                   print(f"Age: {student['Age']}")
                   print(f"course:{student['Course']}")
                   print("-------------------------")
    elif choice == "3":
               search_name = input("Enter student name to search: ")
               found = False
               for student in students:
                     if student["Name"].lower() == search_name.lower():
                           print("\nStudent Found!")
                           print(F"Name: {student['Name']}")
                           print(F"Age: {student['Age']}")
                           print(F"Course: {student['Course']}")
                           found = True
                           break
               if not found:
                           print("Student not found!")
    elif choice == "4":
          update_name = input("Enter student name to update: ")
          found = False
          for student in students:
                if student["Name"].lower() == update_name.lower():
                      student["Age"] = input("Enter new Age: ")
                      student["Course"] = input("Enter new course: ")
                      print("Student updated successfully!")
                      found = True
                      break
          if not found:
              print("student not found!")
    elif choice == "5":
          delete_name = input("Enter student name to delete: ")
          found = False
          for student in students:
                if student["Name"].lower() == delete_name.lower():
                      students.remove(student)
                      print("Student deleted succesfully!")
                      found = True
                      break
          if not found:
                print("Student not found!")

    elif choice == "6":
            print("Thank you for using the Student Management System!")
            break
    else:
          print("invaild choice! please enter a number from 1 to 6")