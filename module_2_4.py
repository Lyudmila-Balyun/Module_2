numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

for i in numbers[1:]:
    is_prime = True
    for j in numbers[1:i-1]:
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(i)
    else:
        not_prime.append(i)

print(prime)
print(not_prime)