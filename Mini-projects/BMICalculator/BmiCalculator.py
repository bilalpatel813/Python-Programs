print("-----------------------------------------------------------")
print()
print("---------------------BMI Calculator------------------------")
print()
def calculateBMI():
    try:
        height = float(input("---------Enter your height (m) : "))
        weight =  float(input("---------Enter your weight(kg) : "))
        
        bmi = weight / (height**2)
        result = round(bmi,2)
        
        if result <=18.5:
            print(f"Your Body Mass Index NO: {result} which is underweight!")
        elif 18.5 < result <= 24.9:
             print(f"Your Body Mass Index NO: {result} which is Normal weight") 
        elif 25<= result <=29.9:
             print(f"Your Body Mass Index NO: {result} which is Overweight")
        elif result >= 30:
             print(f"Your Body Mass Index NO: {result} which is Obese!! ")
        else:
           print("Enter a Valid number for Height in Meters and wight in kilo-grams. ")
           print("Try Again... ")
    except ZeroDivisionError:
           print("Error : Height and Weight must be greater than zero")
    except  ValueError:
        print("Error : please enter an numeric value")
           
def main():
    while True:
        print("-----------------------------------------------------------")
        print()
        print("---------Enter yes/y to calculate BMI ")
        print("---------Enter No/n to Exit ")
    
        user_input = input("enter your task :").lower().strip()
    
        if user_input == "yes" or user_input=="y":
           calculateBMI()
        elif user_input == "no" or user_input=="n":
            print("-----------------------------------------------------------")
            print("come back again...")
            break
        else:
          print("Enter correct task ")
          print("Try Again... ")
          
          
if __name__ == "__main__":
    main()
