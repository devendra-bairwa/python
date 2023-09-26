def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input('Enter a number: '))
print(f'Factorial of {num} is {factorial(num)}')
if is_prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')