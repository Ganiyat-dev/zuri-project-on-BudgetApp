class Budget:
    def __init__(self, bCategory=["food","clothing","entertainment"], balance=[40000, 25000, 10000]):
        #balance at index 0 = foodBalance, index 1 = clothing and index 2 = entertainment
        self.balance = balance
        self.bCategory = bCategory
        print ("These are the available categories: \n 1. Food \n 2. clothing \n 3. Entertainment")
    
    def deposit(self):
        selectedCategory = int(input("Please enter the Category option to continue \n"))
        if selectedCategory not in [1,2,3]:
            print("You must enter option 1, 2 or 3 to continue")
            selectedCategory = int(input("Please enter the Category option to continue \n"))
        if selectedCategory == 1:
            amount = int(input("Enter amount to deposit: \n"))
            self.balance[0] = self.balance[0] + amount
            print("You have successfully deposited %d in your %s." % (self.balance[0], self.bCategory[0]))
        elif selectedCategory == 2:
            amount = int(input("Enter amount to deposit: \n"))
            self.balance[1] = self.balance[1] + amount
            print("You have successfully deposited %d in your %s." % (self.balance[1], self.bCategory[1]))
        elif selectedCategory == 3:
            amount = int(input("Enter amount to deposit: \n"))
            self.balance[2] = self.balance[2] + amount
            print("You have successfully deposited %d in your %s." % (self.balance[2], self.bCategory[2])) 
        else:
            print("You have selected an Invalid category option")

#withdraw money from each category respectively
    def withdraw(self):
        category = int(input("Please enter the Category option to continue: \n"))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select a category option to continue: \n"))
        if category == 1:
            amount = int(input("Enter amount to withdraw: \n"))
            if self.balance[0] < amount:
                print("Insufficient balance")
            else: 
                self.balance[0] = self.balance[0] - amount
                print("Withdrawal successful, your balance remain: ", self.balance[0])
        elif category == 2:
            amount = int(input("Enter amount to withdraw: \n"))
            if self.balance[1] < amount:
                print("Insufficient balance")
            else: 
                self.balance[1] = self.balance[1] - amount
                print("Withdrawal successful, your balance remain: ", self.balance[1])
        elif category == 3:
            amount = int(input("Enter amount to withdraw: \n"))
            if self.balance[2] < amount:
                print("Insufficient balance")
            else: 
                self.balance[2] = self.balance[2] - amount
                print("Withdrawal successful, your balance remain: ", self.balance[2])
        else:
            print("Category option could not be found")
        
    def check_balance(self):
        selectedCategory = int(input("Please enter the Category option to continue: \n"))
        if selectedCategory not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            selectedCategory = int(input("please select a category option to continue: "))
        if selectedCategory == 1:
            print("Your %s BALANCE is: %s " % (self.bCategory[0], self.balance[0])) 
        elif selectedCategory == 2:
            print("Your %s BALANCE is: %s " % (self.bCategory[1], self.balance[1]))
        elif selectedCategory == 3:
            print("Your %s BALANCE is: %s " % (self.bCategory[2], self.balance[2]))
        else:
            print("Invalid category option")

#transfer from current budget category(sending to receiving category)
    def transfer_funds(self):
        category = int(input("Select category to transfer from: \n"))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select category to transfer from: \n"))
        amount = int(input("Enter the amount: \n"))
        rCategory = int(input("Enter category to transfer to \n"))
        while category == rCategory:
            print("You can not transfer to the same category")
            rCategory = int(input("Enter category to transfer to: \n"))
        if rCategory == 1:
            self.balance[category] = self.balance[category] - amount 
            self.balance[rCategory] = self.balance[rCategory] + amount
            print("You have successfully transfered %d" %amount )
        elif(rCategory == 2):
            self.balance[category] = self.balance[category] - amount 
            self.balance[rCategory] = self.balance[rCategory] + amount
            print("You have successfully transfered %d" %amount )
        elif(rCategory == 3):
            self.balance[category] = self.balance[category] - amount 
            self.balance[rCategory] = self.balance[rCategory] + amount
            print("You have successfully transfered %d" %amount)


print ("Welcome to myBudgetApp")
option = int(input("Select the transaction you would like to perform:  \n 1. to deposit \n 2. to withdraw \n 3. for balance Inquiry \n 4. to transfer \n"))
while option not in (1,2,3,4):
    print("Invalid option selected")
    option = int(input("Enter a valid option to continue: "))

budget = Budget()
if option == 1:
    budget.deposit()
    pass
elif option == 2:
    budget.withdraw()
elif option == 3:
    budget.check_balance() 
else:
    budget.transfer_funds()

