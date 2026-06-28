names = []
roll_numbers = []
marks = []
while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print('1)Add student')
    print('2)View student')
    print('3)Search student')
    print('4)Update student')
    print('5)Delete student')
    print('6)EXIT')
    choice = int(input("Enter Your Choice"))
    if choice ==1:
     name = input("Enter Students Name")
     roll_number = int(input("enter roll number"))
     mark = int(input("enter marks"))
     names.append(name)
     roll_numbers.append(roll_number)
     marks.append(mark)
     
     print("STUDENT ADDED SUCCESSFULLY")
     
    elif choice == 2:
     if len(names) == 0:
        print("No students found.")
     else:
        print("--------------------------------")
        print("Roll No.\t\tName\t\tMarks")
        print("--------------------------------")
        print("--------------------------------")
        for i in range(len(names)):
            print(roll_numbers[i],"\t\t", names[i],"\t\t", marks[i])
    elif choice ==3:
        roll_number= int(input("enter roll number to search"))
     #   found = False
        for i in range (len(roll_numbers)):
         if roll_numbers[i] == roll_number :
            print("\nStudent Found!")
            print("Name :", names[i])
            print("Roll Number :", roll_numbers[i])
            print("Marks :", marks[i])
           # found = True 
  #  if found == False:
      #  print("Student Not Found!")
    elif choice == 4:
     roll = int(input("Enter Roll Number to Update: "))
     for i in range(len(roll_numbers)):
        if roll_numbers[i] == roll:
            print("\nCurrent Details")
            print("Name :", names[i])
            print("Marks :", marks[i])
            names[i] = input("Enter New Name: ")
            marks[i] = int(input("Enter New Marks: "))
            print("Student Updated Successfully!")
    elif choice == 5:
     roll = int(input("Enter Roll Number to Delete: "))
     for i in range(len(roll_numbers)):
        if roll_numbers[i] == roll:
            del names[i]
            del roll_numbers[i]
            del marks[i]
            print("Student Deleted Successfully!")
            break
    elif choice == 6:
        print("Thank You, For Visiting !!")
        break
else:
    print("Invalid Choice!")