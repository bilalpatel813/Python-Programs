records =[]
class Student:
    def __init__(self,name,roll,marks,grade):
        self.name= name
        self.roll = roll
        self.marks =marks
        self.grade =grade 
    def fileSave(self):
        with open ("studentrecord.txt","w") as f:
            f.write(f"student name: {self.name}\n")
            f.write(f"student roll no.: {self.roll}\n")
            f.write(f"student marks: {self.marks}\n")
            f.write(f"student grade:{self.grade}\n")
        with open("studentrecord.txt","r") as f:
            print(f.read())
    def showStudent(self):
         print(" NAME: %s \n GRADE : %s "%(self.name,self.grade))
         print("MARKS : %d \n ROLL NO. : %d"%(self.marks,self.roll))
         
print("....BASIC STUDENT RECORD SYSTEM....")         
numofstudent =0            
while numofstudent <1:
         numofstudent =int(input("ENTER NO. OF STUDENT TO RECORD :"))

for i in range(numofstudent):
        print("STUDENT %d"%(i+1))
        name = input("ENTER STUDENT NAME :") 
        roll = int(input("ENTER STUDENT ROLL NO : "))
        marks  = int(input("ENTER STUDENT MARKS :"))
        grade = input("ENTER STUDENT GRADE :")
        records.append(Student(name,roll,marks,grade))
        
print("Record Displayed.")
for record in records:
    record.fileSave()

 