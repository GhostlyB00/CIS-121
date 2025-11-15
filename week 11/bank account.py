class BankAccount:
    def __init__(self,name, initial_balance = 0):
        self.owner = name
        self.balance = initial_balance

    def deposit(self, value):
        self.balance += value
    def withdraw(self, value):
        if value is > self.balance:
            print('insufficent funds')
        
        else:
            print(f'here is your ${value}.')
            self.balance -= value
    def get_balance(self):
        return self.balance   

    def __add__(self, other):
        pass     
        
matt_acc = BankAccount('matt')
matt_acc.deposit(100)
matt_acc.deposit(50)

print(matt_acc.get_balance())


ashley_acc = BankAccount('Ashley', 500)
ashley_acc.deposit(250)

joint_acc = matt_acc + ashley_acc  