def fib(N) -> int:
    if N == 0 or N == 1:
        return 1
    return fib(N - 1) + fib(N - 2)

print(fib(4))  # 5