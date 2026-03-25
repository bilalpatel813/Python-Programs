import pandas as pd
import os
file_name="student_record.xlsx"

def load_data():
    if os.path.exists(file_name):
        return pd.read_excel(file_name)
    else:
        return pd.DataFrame(columns=['Name','Roll no.','Age','Marks','Grade'])
        
def save_data(df):
    return df.to_excel(file_name,index=True) 
     
def add_student(df):
     name=input("enter student name: ")
     roll_no=int(input("enter student roll no. :"))
     age=int(input("enter student age: "))
     marks=int(input("enter student marks"))
     grade=input("enter student grade : ")
     insert={
     "Name":name,
     "Age":age,
     "Roll no.":roll_no,
     "Marks":marks,
     "Grade":grade}
     df= pd.concat([df,pd.DataFrame([insert])],ignore_index=True)
     return df
    
def view_student(df):
       if df.empty:
           print("No Data Found")
       else:
           print("stduent details:")
           print(df)
           
def update_student(df):
       if df.empty:
           print("No data found")
       else:
           print("enter details to update :")
           roll_no=int(input("enter student roll no .: "))
           up_name=input("enter student name:" )
           up_age=int(input("enter student age: "))
           up_marks=int(input("enter student marks: "))
           up_grade=input("enter student grade : ")
           df.loc[df["Roll no."]== roll_no,["Name","Marks","Age",]]=[up_name,up_marks,up_age]
           print("record updated successfully!!")
           return df 
   
def delete_student(df):
           del_roll_no=int(input("enter student roll no. : "))
           df=df[df["Roll no."] !=del_roll_no ]
           print(" record deleted successfully")
           return df
def main():
    df = load_data()
    while True:
        print(" 1. to Add student")
        print(" 2. to view student")
        print(" 3. to update student")
        print(" 4. to delete student")
        print(" 5. to exit program ")
        choice= int(input("ENTER YOUR CHOICE :"))
        if choice ==1:
            df=add_student(df)
            print("student details added successfully!")
        elif choice == 2:
            view_student(df)
        elif choice == 3:
            update_student(df)
        elif choice == 4:
            delete_student(df)
        elif choice == 5:
            save_data(df)
            print("data saved successfully")
            break
        else:
            print("invalid input try again ")
main()