"""
Fibonacci Numbers and Primality
Author: William Nguyen
"""


def fib(n):
   if 0 <= n <= 46:
      Fm, Fn = 1, 0
      for i in range(0, n):
         Fm, Fn = Fn, Fm + Fn
      
      if n % 4 == 0:
         print("Buzz")
         if n % 5 == 0:
            print("Fizz")
      elif n % 5 == 0:
         print("Fizz")
      elif isPrime(n) and isPrime(Fn):
         print("BuzzFizz")
      else:
         print(Fn)
   else:
      print("n must be an integer from 0 to 46")
      Fn = -1

   return Fn

def isPrime(num):
   if num < 2 or (num != 2 and num % 2 == 0) or (num != 3 and num % 3 == 0):
      prime = False
   else:
      prime, i = True, 5
      while i * i <= num and prime:
         if num % i == 0 or num % (i + 2) == 0:
            prime = False
         i += 6

   return prime