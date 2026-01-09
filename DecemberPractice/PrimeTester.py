import os

os.system("clear")

try:
    num = int(input("ENTER A NUMBER TO TEST IF IT IS PRIME: "))
except:
    print("invalid input.")
    exit()

if num < 0:
    print("error. negative integer.")
    exit()
elif num < 2:
    print(f"{num} is not prime.")
    print("no prime numbers less than 2.")
    exit()

primes = []
for i in range(2, num + 1):
    is_prime = True
    # Check divisibility by already found primes up to the square root of i
    for j in primes:
        if j * j > i:
            break
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

# Example usage:
print(f"The prime numbers up to {num} are: {primes}")
