# Working on Validation...Soon it will be uploaded.
"""Student Management System

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Grade
7. Exit"""
def calculategrade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=50:
        return "D"
    else:
        return "Fail"
smanagement={}
while True:
    try:
        print("---------------------------------------------")
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("----------------------------------------------")
        print("Select which operation you want to perform")
        print("1.Add Student")
        print("2.View All Students")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Calculate Grade")
        print("7. Exit")
        print("------------------------------------------------")
        choice=int(input("Enter your choice: "))
        if choice<1 or choice>7:
            print("Invalid Choice")
        else:
            match choice:
                case 1:
                    rollno=int(input("Enter roll no of student : "))
                    if 1 <= rollno <= 100:
                        if rollno in smanagement:
                            print("Student already exists")
                        else:
                            sname=input("Enter Student Name : ")
                            sage=int(input("Enter Student Age : "))
                            smarks=int(input("Enter Student marks : "))
                            if smarks < 0 or smarks > 100:
                                print("Marks should be between 0 and 100")
                            else:
                             smanagement[rollno]={"name":sname,"age":sage,"marks":smarks}
                             print("Student added successfully")
                    else:
                        print("Roll no should be in 1-100 ")
                case 2:
                    if len(smanagement)==0:
                        print("No student added")
                    else:
                        print("total No of Students: ",len(smanagement))
                        for rollno,details in smanagement.items():
                            print("---------------------------------------")
                            print("Roll no: ",rollno)
                            print("Student Name: ",details["name"])
                            print("Student Age: ",details["age"])
                            print("Student Marks: ",details["marks"])
                            print("Grade:", calculategrade(details["marks"]))
                case 3:
                    rollno=int(input("Enter roll no of student : "))
                    if 1 <= rollno <= 100:
                        if rollno in smanagement:
                                details=smanagement[rollno]
                                print("Roll no: ",rollno)
                                print("Student Name: ",details["name"])
                                print("Student Age: ",details["age"])
                                print("Student marks: ",details["marks"])
                                print("Grade:", calculategrade(details["marks"]))
                        else:
                            print("invalid Roll no")
                    else:
                        print("Roll no should be in 1-100 ")
                case 4:
                    rollno=int(input("Enter roll no to update student : "))
                    if 1 <= rollno <= 100:
                        if rollno in smanagement:
                            print("1.update Name")
                            print("2.update Age")
                            print("3.update Marks")
                            up_choice=int(input("what do want to update: "))
                            if up_choice==1:
                                upconfirm=input("Are you sure (y/n):").lower()
                                if upconfirm == "y" or upconfirm=="n":
                                    if upconfirm=="y":
                                        smanagement[rollno]["name"]=input("Enter New Name : ")
                                        print("Student updated successfully")
                                    else:
                                        print("update Operation Canceled")
                                else:
                                    print("Enter yes or no (y/n)")
                            elif up_choice==2:
                                upconfirm = input("Are you sure (y/n):").lower()
                                if upconfirm == "y" or upconfirm=="n":
                                    if upconfirm == "y":
                                        newage=int(input("Enter New Age : "))
                                        if 1 <= newage <= 100:
                                            smanagement[rollno]["age"]=newage
                                            print("Student updated successfully")
                                        else:
                                            print("Enter should be between 1 and 100")
                                    else:
                                        print("update Operation Canceled")
                                else:
                                    print("Enter yes or no (y/n)")
                            elif up_choice==3:
                                upconfirm = input("Are you sure (y/n):").lower()
                                if upconfirm =="y" or upconfirm =="n":
                                    if upconfirm == "y":
                                         newmarks=int(input("Enter New Marks : "))
                                         if 0 <= newmarks <= 100:
                                             smanagement[rollno]["marks"]=newmarks
                                             print("Student updated successfully")
                                         else:
                                             print("Marks Should be between 0 and 100")
                                    else:
                                        print("update Operation Canceled")
                                else:
                                    print("Enter yes or no (y/n)")
                            else:
                                print("Invalid choice")
                        else:
                            print("Invalid Roll no")
                    else:
                        print("Roll no should be in 1-100 ")
                case 5:
                    rollno=int(input("Enter roll no of student : "))
                    if 1 <= rollno <= 100:
                        if rollno in smanagement:
                            confirm=input("Are you sure (y/n):").lower()
                            if confirm=="y":
                                del smanagement[rollno]
                                print("Student removed successfully.")
                            else:
                                print("Delete Operation Canceled")
                        else:
                            print("Invalid Roll no")
                    else:
                        print("Roll no should be in 1-100 ")
                case 6:
                    rollno=int(input("Enter roll no of student : "))
                    if 1 <= rollno <= 100:
                        if rollno in smanagement:
                            marks=smanagement[rollno]["marks"]
                            grade=calculategrade(marks)
                            print("Marks",marks)
                            print("Grade",grade)
                        else:
                            print("Invalid Roll no")
                    else:
                        print("Roll no should be in 1-100 ")
                case 7:
                    print("Thank you for using Student Management System")
                    break
    except ValueError:
      print("Invalid input. Please enter numbers only where required.")
