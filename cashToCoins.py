dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

piggyBank["quarters"] = int(dollarAmount * 4)
piggyBank["dimes"] = int((dollarAmount - piggyBank["quarters"] / 4) * 10)
piggyBank["nickels"] = int((dollarAmount - piggyBank["quarters"] / 4 - piggyBank["dimes"] / 10) * 20)
piggyBank["pennies"] = round((dollarAmount - piggyBank["quarters"] / 4 - piggyBank["dimes"] / 10 - piggyBank["nickels"] / 20) * 100)

print(piggyBank)
