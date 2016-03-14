#!/usr/bin/python3

from BuzzFizz import fib, isPrime


print("Checking n = -1 is invalid input...")
assert fib(-1) == -1
print("Test passed!\n")
print("Checking F(0) is 0...")
assert fib(0) == 0
print("Test passed!\n")
print("Checking F(1) is 1...")
assert fib(1) == 1
print("Test passed!\n")
print("Checking F(2) is 1...")
assert fib(2) == 1
print("Test passed!\n")
print("Checking F(3) is 2...")
assert fib(3) == 2
print("Test passed!\n")
print("Checking F(4) is 3...")
assert fib(4) == 3
print("Test passed!\n")
print("Checking F(5) is 5...")
assert fib(5) == 5
print("Test passed!\n")
print("Checking F(6) is 8...")
assert fib(6) == 8
print("Test passed!\n")
print("Checking F(7) is 13...")
assert fib(7) == 13
print("Test passed!\n")
print("Checking F(8) is 21...")
assert fib(8) == 21
print("Test passed!\n")
print("Checking F(9) is 34...")
assert fib(9) == 34
print("Test passed!\n")
print("Checking F(10) is 55...")
assert fib(10) == 55
print("Test passed!\n")
print("Checking F(11) is 89...")
assert fib(11) == 89
print("Test passed!\n")
print("Checking F(12) is 144...")
assert fib(12) == 144
print("Test passed!\n")
print("Checking F(13) is 233...")
assert fib(13) == 233
print("Test passed!\n")
print("Checking F(14) is 377...")
assert fib(14) == 377
print("Test passed!\n")
print("Checking F(15) is 610...")
assert fib(15) == 610
print("Test passed!\n")
print("Checking F(16) is 987...")
assert fib(16) == 987
print("Test passed!\n")
print("Checking F(17) is 1597...")
assert fib(17) == 1597
print("Test passed!\n")
print("Checking F(18) is 2584...")
assert fib(18) == 2584
print("Test passed!\n")
print("Checking F(19) is 4181...")
assert fib(19) == 4181
print("Test passed!\n")
print("Checking F(20) is 6765...")
assert fib(20) == 6765
print("Test passed!\n")
print("Checking F(21) is 10946...")
assert fib(21) == 10946
print("Test passed!\n")
print("Checking F(22) is 17711...")
assert fib(22) == 17711
print("Test passed!\n")
print("Checking F(23) is 28657...")
assert fib(23) == 28657
print("Test passed!\n")
print("Checking F(24) is 46368...")
assert fib(24) == 46368
print("Test passed!\n")
print("Checking F(25) is 75025...")
assert fib(25) == 75025
print("Test passed!\n")
print("Checking F(26) is 121393...")
assert fib(26) == 121393
print("Test passed!\n")
print("Checking F(27) is 196418...")
assert fib(27) == 196418
print("Test passed!\n")
print("Checking F(28) is 317811...")
assert fib(28) == 317811
print("Test passed!\n")
print("Checking F(29) is 514229...")
assert fib(29) == 514229
print("Test passed!\n")
print("Checking F(30) is 832040...")
assert fib(30) == 832040
print("Test passed!\n")
print("Checking F(31) is 1346269...")
assert fib(31) == 1346269
print("Test passed!\n")
print("Checking F(32) is 2178309...")
assert fib(32) == 2178309
print("Test passed!\n")
print("Checking F(33) is 3524578...")
assert fib(33) == 3524578
print("Test passed!\n")
print("Checking F(34) is 5702887...")
assert fib(34) == 5702887
print("Test passed!\n")
print("Checking F(35) is 9227465...")
assert fib(35) == 9227465
print("Test passed!\n")
print("Checking F(36) is 14930352...")
assert fib(36) == 14930352
print("Test passed!\n")
print("Checking F(37) is 24157817...")
assert fib(37) == 24157817
print("Test passed!\n")
print("Checking F(38) is 39088169...")
assert fib(38) == 39088169
print("Test passed!\n")
print("Checking F(39) is 63245986...")
assert fib(39) == 63245986
print("Test passed!\n")
print("Checking F(40) is 102334155...")
assert fib(40) == 102334155
print("Test passed!\n")
print("Checking F(41) is 165580141...")
assert fib(41) == 165580141
print("Test passed!\n")
print("Checking F(42) is 267914296...")
assert fib(42) == 267914296
print("Test passed!\n")
print("Checking F(43) is 433494437...")
assert fib(43) == 433494437
print("Test passed!\n")
print("Checking F(44) is 701408733...")
assert fib(44) == 701408733
print("Test passed!\n")
print("Checking F(45) is 1134903170...")
assert fib(45) == 1134903170
print("Test passed!\n")
print("Checking F(46) is 1836311903...")
assert fib(46) == 1836311903
print("Test passed!\n")
print("Checking n = 47 is invalid input...")
assert fib(47) == -1
print("Test passed!\n")

print("Checking 0 is not prime...")
assert not isPrime(0)
print("Test passed!\n")
print("Checking 1 is not prime...")
assert not isPrime(1)
print("Test passed!\n")
print("Checking 2 is prime...")
assert isPrime(2)
print("Test passed!\n")
print("Checking 3 is prime...")
assert isPrime(3)
print("Test passed!\n")
print("Checking 4 is not prime...")
assert not isPrime(4)
print("Test passed!\n")
print("Checking 5 is prime...")
assert isPrime(5)
print("Test passed!\n")
print("Checking 6 is not prime...")
assert not isPrime(6)
print("Test passed!\n")
print("Checking 7 is prime...")
assert isPrime(7)
print("Test passed!\n")
print("Checking 8 is not prime...")
assert not isPrime(8)
print("Test passed!\n")
print("Checking 9 is not prime...")
assert not isPrime(9)
print("Test passed!\n")
print("Checking 10 is not prime...")
assert not isPrime(10)
print("Test passed!\n")
print("Checking 11 is prime...")
assert isPrime(11)
print("Test passed!\n")
print("Checking 12 is not prime...")
assert not isPrime(12)
print("Test passed!\n")
print("Checking 13 is prime...")
assert isPrime(13)
print("Test passed!\n")
print("Checking 14 is not prime...")
assert not isPrime(14)
print("Test passed!\n")
print("Checking 15 is not prime...")
assert not isPrime(15)
print("Test passed!\n")
print("Checking 16 is not prime...")
assert not isPrime(16)
print("Test passed!\n")
print("Checking 17 is prime...")
assert isPrime(17)
print("Test passed!\n")
print("Checking 18 is not prime...")
assert not isPrime(18)
print("Test passed!\n")
print("Checking 19 is prime...")
assert isPrime(19)
print("Test passed!\n")
print("Checking 20 is not prime...")
assert not isPrime(20)
print("Test passed!\n")
print("Checking 21 is not prime...")
assert not isPrime(21)
print("Test passed!\n")
print("Checking 22 is not prime...")
assert not isPrime(22)
print("Test passed!\n")
print("Checking 23 is prime...")
assert isPrime(23)
print("Test passed!\n")
print("Checking 24 is not prime...")
assert not isPrime(24)
print("Test passed!\n")
print("Checking 25 is not prime...")
assert not isPrime(25)
print("Test passed!\n")
print("Checking 26 is not prime...")
assert not isPrime(26)
print("Test passed!\n")
print("Checking 27 is not prime...")
assert not isPrime(27)
print("Test passed!\n")
print("Checking 28 is not prime...")
assert not isPrime(28)
print("Test passed!\n")
print("Checking 29 is prime...")
assert isPrime(29)
print("Test passed!\n")
print("Checking 30 is not prime...")
assert not isPrime(30)
print("Test passed!\n")
print("Checking 31 is prime...")
assert isPrime(31)
print("Test passed!\n")
print("Checking 32 is not prime...")
assert not isPrime(32)
print("Test passed!\n")
print("Checking 33 is not prime...")
assert not isPrime(33)
print("Test passed!\n")
print("Checking 34 is not prime...")
assert not isPrime(34)
print("Test passed!\n")
print("Checking 35 is not prime...")
assert not isPrime(35)
print("Test passed!\n")
print("Checking 36 is not prime...")
assert not isPrime(36)
print("Test passed!\n")
print("Checking 37 is prime...")
assert isPrime(37)
print("Test passed!\n")
print("Checking 38 is not prime...")
assert not isPrime(38)
print("Test passed!\n")
print("Checking 39 is not prime...")
assert not isPrime(39)
print("Test passed!\n")
print("Checking 40 is not prime...")
assert not isPrime(40)
print("Test passed!\n")
print("Checking 41 is prime...")
assert isPrime(41)
print("Test passed!\n")
print("Checking 42 is not prime...")
assert not isPrime(42)
print("Test passed!\n")
print("Checking 43 is prime...")
assert isPrime(43)
print("Test passed!\n")
print("Checking 44 is not prime...")
assert not isPrime(44)
print("Test passed!\n")
print("Checking 45 is not prime...")
assert not isPrime(45)
print("Test passed!\n")
print("Checking 46 is not prime...")
assert not isPrime(46)
print("Test passed!\n")
print("Checking 47 is prime...")
assert isPrime(47)
print("Test passed!\n")
print("Checking 121 is not prime...")
assert not isPrime(121)
print("Test passed!\n")

print("All tests passed!")