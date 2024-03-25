
userInput = float(input("Enter a purchase price: "))

def calculations():
    balance = userInput - userInput * 0.1
    print("Balance   Interest   Principal   Payment   New Balance")

    while balance > 0:
        interest = (balance * 0.12) / 12
        principal = (balance - balance * 0.2) * 0.05
        payment = principal + interest
        balance -= payment
        print("%.2f" % balance, "    ", "%.2f" % interest, "    ", "%.2f" % principal, "    ", "%.2f" % payment, "    ", "%.2f" % balance)
    
calculations()
