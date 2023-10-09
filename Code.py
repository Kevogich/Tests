import random
import math

random_numbers = [random.randint(1, 100) for _ in range(10)]
logarithms = [math.log(num) for num in random_numbers]

print(logarithms)


def prime_numbers(n):
    primes = []
    for num in range(2, len(n)):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes
list1 = [random.randint(1, 100) for _ in range(59)]
print (list1)
print (prime_numbers(list1))