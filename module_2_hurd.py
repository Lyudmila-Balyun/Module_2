def find_pairs_for_n(n):
    result = ''
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if (a + b) % n == 0:
                result += f"{a}{b}"
    return result


n = int(input("Введите число из первой вставки (от 3 до 20): "))

password = find_pairs_for_n(n)
print(f"Нужный пароль для {n}: {password}")