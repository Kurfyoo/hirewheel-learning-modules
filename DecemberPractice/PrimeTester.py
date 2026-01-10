import os

os.system("clear")

try:
    num = int(input("ENTER A NUMBER TO TEST IF IT IS PRIME: "))
except:
    print("invalid input.")
    exit()

if num < 0:
    print("no negative integers.")
    exit()
elif num < 2:
    print(f"{num} is not prime.")
    print("no primes less than 2.")
    exit()
elif num == 2:
    print(f"{num} is prime.\nprimes up to {num}: [2]")
    exit()

primes = []
for i in range(3, num + 1,2):
    is_prime = ""
    # Check divisibility by already found primes up to the square root of i
    for j in primes:
        if j * j > i:
            break
        if i % j == 0:
            is_prime = "not "
            break
    if not is_prime:
        primes.append(i)

# Example usage:
print(f"{num} is {is_prime}prime.\nprimes up to {num}: {primes}")
