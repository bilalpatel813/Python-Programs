import datetime
list=[]
class credits:
    amount=0
    name=""
    AA=0
    SA=0
    credit=0
    time=0
    def Add(self):
        self.credit=self.amount+ self.AA
        return self.credit
        list.append(self.credit)
    def sub(self):
        self.credit=self.amount- self.SA
        return self.credit
        list.append(self.credit)
    def againAdd(self):
        self.credit=self.credit + self.AA
        return self.credit
        list.append(self.credit)
    def againSubtract(self):
        self.credit=self.credit - self.SA
        return self.credit
        list.append(self.credit)

    def identity(self):
        self.Name=name
        return self.Name
    def timing(self):
        self.time=datetime.date.today()
        return self.time
    def getInfo(self):
         print(" NAME: %s \n credit: %d   "%(self.name,self.credit))
         print(f"TIME : {self.time}")

obj= credits()
while True:
       if obj.amount<1:
           obj.name=input("ENTER NAME: ")
           obj.amount=int(input("ENTER AMOUNT OF CREDIT : "))
           obj.timing()
           print( "  type 1 : for ADD")
           print( "  type 2 : for SUBTRACT")
           print( "  type 3 : for AGAIN ADD")
           print( "  type 4 : for AGAIN SUBTRACT")
       choice=int(input("enter no. for task(1/2/3/4):  "))
       if choice ==1:
                obj.AA=int(input("ENTER AMOUNT TO ADD : "))
                obj.Add()
                obj.timing()
                obj.getInfo()
           
       elif choice ==2:
                obj.SA=int(input("ENTER AMOUNT TO SUBTRACT :"))
                obj.sub()
                obj.timing()
                obj.getInfo()
        
       elif choice ==3:
                obj.AA=int(input("ENTER AMOUNT TO ADD :"))
                obj.againAdd()
                obj.timing()
                obj.getInfo()
       
       elif choice ==4:
                obj.SA=int(input("ENTER AMOUNT TO SUBTRACT :"))
                obj.againSubtract()
                obj.timing()
                obj.getInfo()        
                
                              
                              
                              
             