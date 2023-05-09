def is_prime(num):
    if num <= 1:
        return False
    limit = int(num ** 0.5)
    for i in range(2, limit + 1):
        if num % i == 0:
            return False
    return True
