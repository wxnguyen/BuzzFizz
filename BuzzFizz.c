/* Fibonacci Numbers and Primality
   Author: William Nguyen */

#include <stdio.h>
#include "BuzzFizz.h"

#define TRUE 1
#define FALSE 0


// Function to generate Fibonacci sequence and print messages
// dependent upon divisibility and primality of F(n)
int fib(int n) {
   int Fn, a, tmp;

   if (n >= 0 && n <= 46) {
      // Determine value of F(n), where 0 <= n <= 46
      Fn = 0; // F(0)
      a = 1;
      while (n-- > 0) {
         tmp = Fn;
         Fn += a;
         a = tmp;
      }

      // Determine divisibility or primality of F(n)
      if (Fn % 3 == 0) {
          printf("Buzz\n");
          if (Fn % 5 == 0) {
              printf("Fizz\n"); // Divisibility by both 3 and 5
          }
      } else if (Fn % 5 == 0) {
          printf("Fizz\n");
      } else if (isPrime(Fn)) {
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

   if (num < 2 || (num != 2 && num % 2 == 0)) {
      prime = FALSE;
   } else {
      prime = TRUE;
      // Could set i = 7 to save 2 iterations since fib() already
      // checks for divisibility by 3 and 5, but i = 3 so
      // that isPrime() can be a stand-alone function.
      for (i = 3; i * i <= num && prime; i += 2) { 
         if (num % i == 0) {
            prime = FALSE;
         }
      }
   }

   return prime;
}