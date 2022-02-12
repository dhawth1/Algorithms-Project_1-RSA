import math
import random

 
p = 7
q = 17
n=p*q
e = 5
wp=(p-1)*(q-1)
d=77

def generatePrime():
   
    while True:
             
            a = random.randint(1000000, 9999999999)
               
            # Fermat's little theorem
            if pow(a, n - 1, n) == 1:
                break
            
    return a

def generateE(e,y):
   
    while True:
             
            a = random.randint(2, 100)
            y=(p-1)*(q-1)
            # Fermat's little theorem
            if math.gcd(a,y)== 1:
                break
            
    return a
def extended_gcd(a=1, b =1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d
 
   


def fastExpo_recursive(a, p, n):
    ''' Returns a^p mod n '''
    if p == 0:
        return 1
    if p%2 == 0:
        t = fastExpo_recursive(a, p//2, n)
        return (t*t)%n
    else:
        t = fastExpo_recursive(a, p//2, n)
        return a *(t**2%n)%n

 
def encrypt(me):
    en = math.pow(me,e)
    c = en % n
    # c=fastExpo_recursive(me,e,n) 
    c=pow(me,d,n) 
    return c

def decrypt(me):
    # c=fastExpo_recursive(me,d,n)
    c=pow(me,d,n) 
    return c
