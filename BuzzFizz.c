/* Fibonacci Numbers and Primality
   Author: William Nguyen */

#include <stdio.h>
#include "BuzzFizz.h"

#define TRUE 1
#define FALSE 0


// Function to generate nth Fibonacci number and print messages
// dependent upon divisibility and primality of F(n)
int fib(int n) {
   int Fn, i, a, tmp;

   if (n >= 0 && n <= 46) {
      // Determine value of F(n), where 0 <= n <= 46
      Fn = 0; // F(0)
      a = 1;
      i = n;
      while (i-- > 0) {
         tmp = Fn;
         Fn += a;
         a = tmp;
      }

      // F(n) is divisible by F(k) if n is a multiple of k. Thus
      // divisibility by 3 and 5 can be determined without calculating F(n).
      // Since F(4) = 3, if n is divisible by 4, F(n) is divisible by 3.
      if (n % 4 == 0) { //
         printf("Buzz\n");
         // Since F(5) = 5, if n is divisible by 5, F(n) is divisible by 5.
         if (n % 5 == 0) {
            printf("Fizz\n"); // Divisibility by both 3 and 5
         }
      } else if (n % 5 == 0) {
         printf("Fizz\n");
      // When F(n) is prime, n is also prime.
      // For the current implementation of isPrime(), it is more efficient
      // to check for primality of n since n is orders of magnitude smaller
      // than F(n) when n is large. If n is not prime, the if statement will
      // short-circuit and isPrime(Fn) will not be evaluated.
      } else if (isPrime(n) && isPrime(Fn)) {
         printf("BuzzFizz\n");
      } else {
         printf("%d\n", Fn);
      }
   } else {
      printf("n must be an integer from 0 to 46\n");
      Fn = INVALID_INPUT;
   }

   return Fn;
}

int isPrime(int num) {
   int i, prime;

   if (num < 2 || (num != 2 && num % 2 == 0) || (num != 3 && num % 3 == 0)) {
      prime = FALSE;
   } else {
      prime = TRUE;
      // The modulo operation should be skipped for
      // every i that is even or a multiple of 3.
      for (i = 5; i * i <= num && prime; i += 6) { 
         if (num % i == 0 || num % (i + 2) == 0) {
            prime = FALSE;
         }
      }
   }

   return prime;
}