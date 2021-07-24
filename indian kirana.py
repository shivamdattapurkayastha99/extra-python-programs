# write a python program which will keep adding a stream of numbers entered by user the adding stops 
# as soon as user presses enter 
sum=0
while True:
    userInput=input("Enter the price and press q to quit")
    if userInput!='q':
        sum=sum+int(userInput)
    else:
        print(f"the sum is {sum}")
        break

    
