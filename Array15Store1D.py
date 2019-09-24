from random import randint

def init():
    return(0)

def EnterData():
    s = []
    for r in range(15):
        s.append(randint(0,100))
    return(s)
        
def CalcPercent(sales,summation):
    P = []
    for r in range(15):
        summation = summation + sales[r]
    for r in range(15):
        P.append([])
        P[r] = sales[r]/summation*100
    return(P)

def Report(sales,Percent):
    print("="*22)
    print(f"|{'No.':>4}|{'Sales':>6}|{'Percent':>8}|")
    print("="*22)
    for r in range(15):
        print(f"|{r+1:>4}|{sales[r]:>6}|{Percent[r]:>8.2f}|")
    print("="*22)

    
#main
summation = init()
sales = EnterData()
Percent = CalcPercent(sales,summation)
Report(sales,Percent)
