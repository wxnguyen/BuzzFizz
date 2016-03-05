/* Fibonacci Numbers and Primality
   Author: William Nguyen */

#include <stdio.h>
#include <stdlib.h>
#include "BuzzFizz.h"

#define TRUE 1
#define FALSE 0


// int isPrime(unsigned int num);

// Function to generate Fibonacci sequence and print messages
// dependent upon divisibility and primality of F(n)
unsigned int fib(unsigned int n) {
   int i;
   unsigned int Fn, *seq; // unsigned to correctly interpret F(47)

   seq = malloc(sizeof(unsigned int) * (n + 1));

   // Generate first n Fibonacci numbers, where 0 <= n <= 47
   seq[0] = 0; // F(0) = 0
   if (n > 0) {
      seq[1] = 1; // F(1) = 1
      for (i = 2; i <= n; i++) {
         seq[i] = seq[i - 1] + seq[i - 2];
         //printf("F(%d) is %u\n", i, seq[i]); // For debugging
      }
   }
   Fn = seq[n];

   // Determine divisibility or primality of F(n)
   if (Fn % 3 == 0) {
       printf("Buzz");
       if (Fn % 5 == 0) {
           printf("Fizz"); // Divisibility by both 3 and 5
       }
   } else if (Fn % 5 == 0) {
       printf("Fizz");
   } else if (isPrime(Fn)) {
      printf("BuzzFizz");
   } else {
      printf("%u", Fn);
   }
   printf("\n");

   free(seq);
   return Fn;
}

int isPrime(unsigned int num) {
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
