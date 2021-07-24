# 20 random cards are placed in a row all face down.A move consists of turning a face down card,face up
# and turning over the card immidiately to the right.Show that no matter what the choice of cards to turn 
# this sequence of moves must terminate
def transform(a):
    for i in range(len(a)-1):
        if a[i]=='1':
            a[i]='0'
            if a[i+1]=='0':
                a[i+1]='1'
            else:
                a[i+1]='0'
    return a
if __name__ == "__main__":
    a=list("1100")
    print(a)
    while a!=transform(a.copy()):
        a=transform(a.copy())
    print(a)
    