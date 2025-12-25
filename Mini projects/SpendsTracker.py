import datetime 
list = []
class moneycheck:
    TA = 0 # past amount 
    AA = 0 # adding amount
    TS = 0 # sutracting amount 
    TD =  0 # total display
    aA = 0 # again add 
    aS = 0 # again subtract 
    IN = 0 # income display
    SP= 0 # spends display 
    def add(self):
        global list
        self.TD= self.TA + self.AA
        return self.TA + self.AA 
        return list.append(self.TA)
    def subtract(self):
        self.TD = self.TA - self.TS
        return self.TD
        return list.append(self.TD)
    def againadd(self):
        self.TD = self.TD + self.aA
        return self.TD
        return list.append(self.TD)
    def againsubtract(self):
        self.TD = self.TD - self.aS
        return self.TD
        return list.append(self.TD)
    def income(self):
            if self.aA >0:
                self.IN = self.AA + self.aA
                return self.IN 
            elif self.aA ==0:
                self.IN = self.AA
                return self.IN     
    def spends(self):
            if self.aS >0:
                self.SP = self.TS + self.aS
                return self.SP
            elif self.aS ==0:
                self.IN = self.TS
                return self.SP
    def saveFile(self):
        today = datetime.date.today()
        day = today.strftime("%A")
        with open(date,"w+") as f:
            f.write(f"---------------------------------------------------------\n       DATE : {today} \t DAY : {day} \n \t \t PAST AMOUNT : {self.TA}\n \t \t TOTAL SPENDS:  {self.SP}\n \t \t TOTAL INCOME : {self.IN}\n \t \t FINAL AMOUNT : {self.TD}\n --------------------------------------------------------")
        with open(date,"r") as R:
            print(R.read()) 
            return self.TD       
    def display(self):
        print("AMOUNT: %d"%(self.TD))
abc= moneycheck()
while True:
    if abc.TA <1:
        abc.TA = int(input("enter total amount : "))
    print( "  type 1 : for ADD")
    print( "  type 2 : for SUBTRACT")
    print( "  type 3 : for AGAIN ADD")
    print( "  type 4 : for AGAIN SUBTRACT")
    print("  type 5 : TO SAVE IN FILE ")

    choice= int(input("enter number for task (1/2/3/4/5): "))
   
           
    if choice ==1:
        abc.AA = int(input("ENTER AMOUNT TO ADD: " ))
        abc.add()
        abc.display()
    elif choice == 2:
        abc.TS= int(input("ENTER NUMBER TO SUBTRACT : "))
        abc.subtract()
        abc.display()
    elif choice == 3:
        abc.aA = int(input("ENTER AMOUNT TO ADD AGAIN : " ))
        abc.againadd()
        abc.display()
    elif choice == 4:
         abc.aS= int(input("ENTER AMOUNT TO SUBTRACT AGAIN : "))
         abc.againsubtract()
         abc.display() 
    elif choice == 5:
              date = input("enter file name to save:  ")
              abc.income()
              abc.spends()
              abc.saveFile()
              print(f" \t saved in file {date} successfully")
              break
               
        
                      