def prime_factors(n):
    result = ""
    factor = 2

    while n > 1:
        times = 0
        while n % factor == 0:
            times += 1
            n = n // factor
        if times:
            result += f"({factor}{f'**{times}' if times > 1 else ''})"

        factor += 1

    return result
