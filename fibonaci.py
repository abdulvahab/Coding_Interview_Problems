
from math import log,sqrt

sqrt5 = sqrt(5)
Phi = (1+sqrt5)/2   #Golden ratio
phi = Phi-1         #Golden ratio-1

def fibonaci_at(i):
    # Generates fibonaci of ith rank using Binte's formula using golden ration(phi)
    x = pow(Phi,i)/sqrt5
    y = pow(-phi,i)/sqrt5
    fn = round(x-y)
    if i > 40:
        fn= float(fn)
    return fn

def fibonaci_series_i(sindex=0,findex=20):
    #This function return fibonaci numbers between two indecis ,Default i 0 and 20.
    series = []
    for i in range(sindex,findex+1):
        fn=fibonaci_at(i)
        series.append(fn)
    return series

def fibonaci_series_r(s=0,e=1000):
    # Generates the fibonaci series between given two number or first n `Fibonnaci numbers`
    if s==0:
        fib_num,next_number = 0,1
        series=[0]
    else:
        series=[]
        i = round((2*log(s)+log(5))/(2*log(Phi)))  # i is the closest index of fibonaci number of lower range s
        fib_num,next_number = fibonaci_at(i),fibonaci_at(i+1)
    while next_number <= e:
        fib_num += next_number
        fib_num, next_number = next_number, fib_num
        if fib_num >= s:
            series.append(fib_num)
    return series

def is_fibonaci(number):
    #boolean test to check if a given number is belongs to fibonaci sequence or not
    test1,test2 = 5*pow(number,2)+4, 5*pow(number,2)-4
    if (sqrt(test1).is_integer()) or  sqrt(test2).is_integer():
        return True
    else:
        return False

def adjacent_fibonaci(fn):
    #given a fibonaci number this function determine the previous and next fibonaci number
    if is_fibonaci(fn) == True:
        prev_number = round(fn/Phi)
        next_number = round(fn * Phi)
        return prev_number,next_number
    else:
        return f'\nEnter Valid Fibonaci number, {fn} is not valid Fibonaci number'

def index_of(fn):
    #this function return index of given fibonaci number(check validity using function is_fibonaci)
    if is_fibonaci(fn) == True:
        index = 0
        a,b = 0,1
        while a != fn:
            a,b = b,a+b
            index += 1
        return index
    else:
        return f'\nEnter Valid Fibonaci number, {fn} is not valid Fibonaci number'

if __name__ == "__main__":
    print(fibonaci_series_i(0,10))
    print(fibonaci_series_r(0,1000))
    print(fibonaci_series_r(10,250))
    print(is_fibonaci(89))
    print(index_of(21))
    print(fibonaci_at(6))
    print(adjacent_fibonaci(21))
