
database = {}
#balance = 0

class Budget:
    def __init__(self, category, balance):
        self.category = category
        #self.amount = amount
        self.balance = balance
    
    #instance methods
    def depositFunds(self):
        self.depositAmount = int(input("How much do you want to deposit?\n"))
        self.newBalance = self.depositAmount + self.balance
        print ("%d was deposited. New balance is %d" %(self.depositAmount, self.newBalance))
        self.balance = self.newBalance

    def withdrawFunds(self):
        self.withdrawalAmount = int(input("How much do you want to withdraw?\n"))
        if (self.withdrawalAmount > self.newBalance):
            print ("Insufficient funds")
        elif (self.withdrawalAmount <= self.newBalance):
            self.newBalance -= self.withdrawalAmount
            print ("%d was withdrawn. Balance is %d" %(self.withdrawalAmount, self.newBalance))
            self.balance = self.newBalance

    def categoryBalances(self):
        print("Balance is %d" %self.balance)

    def transferBalanceAmount(self):
        self.transferBalance = int(input("How much do you want to transfer?\n"))
        if (self.transferBalance > self.newBalance):
            print ("Insufficient funds to transfer")
        elif (self.transferBalance <= self.newBalance):
            self.newBalance -= self.transferBalance
            print ("%d was transferred. Balance is %d" %(self.transferBalance, self.newBalance))
            self.balance = self.newBalance



categoryA = Budget("food",1000)
categoryB = Budget("clothing",1000)
categoryC = Budget("entertainment",1000)    

categoryA.depositFunds()
categoryA.withdrawFunds()
categoryA.categoryBalances()