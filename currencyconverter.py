with open('currency.txt','r') as f:
    lines=f.readlines()
# print(lines)
currencyDict={}
for line in lines:
    parsed=line.split("=")
    currencyDict[parsed[0]]=parsed[1]
# print(currencyDict)

print(f"The available options are {currencyDict.keys()}")
amount=int(input("Enter the amount to be converted"))
currency=input("Enter one of these currencies")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")

