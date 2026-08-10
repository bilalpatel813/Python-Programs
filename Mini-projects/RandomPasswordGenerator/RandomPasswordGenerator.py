import random
import string
print("------------------------------------------------------------")
print()
print("-----------------Random Password Generator------------------")
print()
def GetType():
    print("\nSelect Any two Character type for password")
    print("UpperCase, LowerCase, Numbers, Symbols \n")
    char_type = input("Type your any two option : ").lower().split()

    if set(char_type) == {"uppercase", "lowercase"}:
      pass_type = string.ascii_letters

    elif set(char_type) == {"numbers", "symbols"}:
        pass_type = string.digits + string.punctuation
    elif set(char_type) == {"uppercase","numbers"}:
        pass_type = string.digits + string.ascii_uppercase
    elif set(char_type) == {"uppercase","symbols"}:
        pass_type = string.ascii_uppercase + string.punctuation
    elif set(char_type) == {"lowercase","numbers"}:
        pass_type = string.digits + string.ascii_lowercase
    elif set(char_type) == {"lowercase","symbols"}:
        pass_type = string.ascii_lowercase + string.punctuation
    else:
        print("Invalid choice")
        return None
    return pass_type
        
def GeneratePass():
    print("\nChoose Your Password Length")
    pass_length= int(input("enter number from 1-8: "))
    if pass_length> 8:
        print("please enter number from 1-8 ")
        return 
    Type = GetType()
    if Type is None:
        return 
    password = "".join(random.choice(Type)
    for _ in range(pass_length)
    )
    print()
    print("Generated password : ",password)

def main():
    while True:
        print("\nenter Yes/y to Generate password")
        print("enter NO/n to exit")
        print()
        user_input = input("enter your task : ").lower()
        if user_input == "yes" or user_input =="y":
            GeneratePass()
        elif user_input == "no" or user_input =="n":
            print("come back again..")
            break
        else:
            print("enter a valid task to generate password.")
            
            
if __name__ == '__main__':
    main()
    

