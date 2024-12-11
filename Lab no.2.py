def deposit(num):
    global balance
    balance+=num

def withdrawal(num):
    global balance
    balance-=num

balance=0
a=0
d=[]
w=[]
num=0
W=0
D=0

while a!="Exit":
    a=input("Enter W for withdrawal\nEnter D for deposit\nEnter 'Exit' to view the passbook..\n")
    if(a=="W" or a=="w"):
        b=int(input("Enter withdrawal amount :"))
        if balance>b:
            w.append(b)
            withdrawal(b)
        else:
            print("You don't have Sufficient Balance.\nPlease Try Again Later\n")
    elif(a=="D" or a=="d"):
        c=int(input("Enter Deposit amount :"))
        deposit(c)
        d.append(c)

print("Your balance: ",balance)
print("Deposited Amount",d)
print("Withdrawal Amount",w)
