class budget_category:
    account = []
    balance = 0
    name = ""

    def __init__(self, name):
        self.name =  name

    def deposit(self, amount, description =""):
        account.append({"amount": amount, "description": description})


    def withdraw(self, amount, description = ""):
        if amount > self.balance:
            return False
        


    def check_balance(self, amount, description):
        pass


    def transfer_funds(self, amount, description):
        pass



#deposit
#withdraw
#checkBalance
#sendMoney