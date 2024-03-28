# Create Account class with 2 attributes - balance & account no.
# Create method for debit,credit & printing the balance.

class Account:
    
    def __init__(self,bal,acc,name):
        self.name = name
        self.balance = bal
        self.account_no = acc


    # debit method
    def debit(self,amount,name):
        self.name = name
        self.balance -= amount
        print("Rs" , amount,"was debited from your account",name)
        print("total balance = ",self.get_balance())


    # credit method    
    def credit(self,amount,name):
        self.name = name
        self.balance += amount
        print("Rs" , amount,"was credited from your account" ,name )
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance     


acc1 = Account(10000 , 12345 , "chirag")   
acc1.debit(1000,"chirag")
acc1.credit(5000,"chirag")     
        