import time
class Teacher:
    def setfname(self, fname):
        self.fname = fname
    def getfname(self):
        return self.fname
    def setlname(self, lname):
        self.lname = lname
    def getlname(self):
        return self.lname
    def print_details(self):
        return f"First name: {self.fname}\nLast name: {self.lname}\n"
    def print_fdetails(self):
        return f"First name: {self.fname}\nLast name: {self.lname}\nEmail: {t.email}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"
    @email.setter
    def email(self, string):
        _split = string.split("@")[0]
        name = _split.split(".")
        self.fname = name[0]
        self.lname = name[1]
class Student(Teacher):
    def setclass(self, classs):
        self.classs = classs
    def getfname(self):
        return self.classs
    def print_details(self):
        return f"First name: {self.fname}\nLast name: {self.lname}\nClass: {s.classs}\n"
    def print_fdetails(self):
        return f"First name: {self.fname}\nLast name: {self.lname}\nClass is {s.classs}\nEmail: {s.email}"
def main_menu():
    try:
        s_option = int(input("1.To Register a new Student or Teacher\n2.To Check Registered Student or Teacher\n"))
    except Exception as e:
        print("Please Select Option as 1 or 2\n")
    if s_option==1:
        try:
            option = input("1.Student Registration\n2.Teacher Registration\n  ")
        except Exception as e:
            print("Please Select Option as 1 or 2\n")
        if option=="1":
            full_info = input("Please Enter Fname, Lname and class by giving . after each condition\n")
            s = Student()
            if "." in full_info:
                infoo = full_info.split(".")
                fname = infoo[0]
                lname = infoo[1]
                classs = infoo[2]

            else:
                print("please separate every condition by '.' ")
                main_menu()
            try:
                s.setfname(fname)
                s.setlname(lname)
                s.setclass(classs)
            except Exception as e:
                print("Please full fill all condition")
            confirmation = input(f"You Have Entered {s.print_details()}\nPress y if you want to complete registration else press n to exit\n")
            if confirmation=="y":
                print("Please Wait.......")
                time.sleep(1)
                print("Creating Email.....")
                time.sleep(1)
                with open("Student.txt", "a") as op:
                    op.write(s.print_fdetails() + f"\n---------------------------------------------------------------------------------------------")
                print("Registration Done")
                print(f"Your Email is: {s.email}\nPlease Save Your Email")
                main_menu()
            else:
                print("Thanks For Visiting")
                main_menu()
        elif option=="2":
            t = Teacher()
            full_info = input("Please Enter Fname and Lname by giving . after each condition\n")
            if "." in full_info:
                infoo = full_info.split(".")
                fname = infoo[0]
                lname = infoo[1]
            else:
                print("please separate every condition by '.' ")
                main_menu()
            try:
                t.setfname(fname)
                t.setlname(lname)
            except Exception as e:
                print("Please full fill all condition")
            confirmation = input(f"You Have Entered {t.print_details()}\nPress y if you want to complete registration else press n to exit\n")
            if confirmation=="y":
                print("Please Wait.......")
                time.sleep(1)
                print("Creating Email.....")
                time.sleep(1)
                with open("Teacher.txt", "a") as op:
                    op.write(t.print_fdetails() + f"\n---------------------------------------------------------------------------------------------")
                print("Registration Done")
                print(f"Your Email is: {t.email}\nPlease Save Your Email")
                main_menu()

            else:
                print("Thanks For Visiting")
                main_menu()
        else:
            print("Please enter anyone option")
            main_menu()

    elif s_option==2:
        try:
            check = int(input("1.To Check Student is Registered or not\n2.To Check Teacher is Registered or not\n"))
        except Exception as e:
            print("Please Select Option as 1 or 2\n")
        if check==1:
            f = open("Student.txt", "r")
            str = f.read()
            email_enter = input("Enter Email of student to check\n")
            if email_enter in str:
                infoo = email_enter.split("@")[0]
                split_info = infoo.split(".")
                fname = split_info[0]
                lname = split_info[1]
                print("Please wait checking....")
                time.sleep(2)
                print(f"{fname} {lname} is registered\n")
                main_menu()
            else:
                print("No such Student is found\n")
                main_menu()

        elif check==2:
            f = open("Teacher.txt", "r")
            str = f.read()
            email_enter = input("Enter Email of Teacher to check\n")
            if email_enter in str:
                infoo = email_enter.split("@")[0]
                split_info = infoo.split(".")
                fname = split_info[0]
                lname = split_info[1]
                print("Please wait checking....")
                time.sleep(2)
                print(f"{fname} {lname} is registered\n")
                main_menu()
            else:
                print("No such Teacher is found\n")
                main_menu()
        else:
            print("Thanks For Using...\n")
            main_menu()
main_menu()

a = input()