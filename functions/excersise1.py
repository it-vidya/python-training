def getWallet(balance, uname):
    def deposit(amt):
        nonlocal balance
        balance+=amt
        print("deposited, new Balance: ", balance )
    return deposit
c = getWallet(100, "jai")
c(100)
