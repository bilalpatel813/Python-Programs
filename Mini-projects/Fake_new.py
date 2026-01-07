import random

names= [
  "Sharukh Khan",
  "The Cat",
  "Salman Khan",
  "PM Modi ",
  "Shaikh Adnan",
  "Faiz Bhai "
]
done =[
   "Eats Bhel Puri And Danced Bangra like Punjabis",
   "Arrives at station and ask for help",
   "prposed his cush and gets married at  old age",
   "has just launch missile  ",
   "is the toppper of the class",
   "singing salmon bhai ke aage koi kuch bol skta hai kya "
]
place =[
  "at bandstand ",
  "in kurla",
  "at russia ",
  "in ismail yusuf colllege only!!!",
  "in new york",
  "in the principle office front of tripathi sir"
]
while True:
    name= random.choice(names)
    dones= random.choice(done)
    places= random.choice(place)
    user_input = input("DO YOU WANT TO READ ANOTHER NEWS??. (YES/NO) :- ").lower().strip()
    if user_input ==  "yes":
        headline= f"BREAKING NEW!!! :-  {name}{dones} {places} ."
        print( headline)
    elif user_input =="no":
        print(" THANKS FOR READING FAKE NEW AND HAVE A FUN DAY!!")
        break
 