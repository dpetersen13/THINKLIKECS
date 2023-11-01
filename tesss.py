def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_triangle(n):
    current_num = 2
    for i in range(1, n + 1):
        for j in range(i):
            while not is_prime(current_num):
                current_num += 1
            print(current_num, end=" ")
            current_num += 1
        print()

n = int(input("Enter the number of rows for the prime triangle: "))
print_prime_triangle(n)
