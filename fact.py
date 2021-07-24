# calculate the factorial of a given no
# find the no of trailing zeroes in the factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def factorialtrailingzeroes(n):
    count=0
    i=5
    while(n//i!=0):
        count+=int(n/i)
        i=i*5
    return count
    
if __name__ == "__main__":
    n=int(input("Enter the number"))
    factorial=fact(n)
    tz=factorialtrailingzeroes(n)
    print(f"the factorial is {factorial}")
    print(f"the no of trailing zeroes  is {tz}")
