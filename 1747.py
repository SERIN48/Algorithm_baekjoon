#소수 & 팰린드롬

import math

n = int(input("N: "))
m = 1000001

#소수인지 판별하는 함수
def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

#팰린드롬 
def isPalindrome(n) :
    num = str(n)
    
   
    if n == num[::-1]:
        return True
    else :
        return False

while True :
    if isPalindrome(n) :
        if isPrime(n) :
            print(n)
            exit(0)
    n += 1
            