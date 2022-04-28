#더하기 사이클

n = int(input("0보다 크거나 같고 99보다 작거나 같은 정수를 입력하시오. "))

if n < 0 or n > 99 :
    print("Input Error")
    quit()
    
if n < 10 :
    num = "0"+str(n)
    print(num)

def numCycle() :
    