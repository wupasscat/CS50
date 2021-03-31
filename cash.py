while (True):
    quarter = 25
    dime = 0
    nickel = 5
    penny = 1
    coins = 0
    changeInput = input("Change owed: ")
    inputCheck = changeInput.strip(".")
    if inputCheck.isnumeric():
        usrInput = changeInput.strip("$")
        floatInput = float(usrInput)
        if floatInput > 0.00:
            cents = int(floatInput * 100)
            while(cents >= 25):
                cents -= 25
                coins += 1
            while(cents >= 10):
                cents -= 10
                coins += 1
            while(cents >= 5):
                cents -= 5
                coins += 1
            while(cents >= 1):
                cents -= 1
                coins += 1
            print("Coins: ", coins)
        else:
            print("(!) Please input a number above 0")
    else:
        print("(!) Please input a valid number")