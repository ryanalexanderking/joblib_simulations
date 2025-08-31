import time

from joblib import Parallel, delayed


nums_to_square = [n for n in range(1, 11)]

primes = [
    100000000000031,
    100000000000067,
    100000000000097,
    100000000000099,
    100000000000133,
    100000000000139,
    100000000000169,
    100000000000183,
    100000000000261,
    100000000000357,
    100000000000367,
    100000000000403,
    100000000000423,
    100000000000469,
    100000000000487,
    100000000000493,
    100000000000541,
    100000000000601,
    100000000000643,
    100000000000657,
    100000000000709,
    100000000000721,
    100000000000753,
    100000000000777,
    100000000000807,
    100000000000841,
    100000000000843,
    100000000000861,
    100000000000963,
    100000000000993
]

def slow_square(n):
    time.sleep(1)
    return n * n

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print("----- I/O BOUND -----")
print("Standard")
start_time = time.time()
for n in nums_to_square:
    slow_square(n)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print()

print("Joblib Loky Execution")
start_time = time.time()
parrallel_obj = Parallel(n_jobs=-1, backend="loky")
my_squares = parrallel_obj(delayed(slow_square)(n) for n in nums_to_square)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print()

print("Joblib Threaded Execution")
start_time = time.time()
parrallel_obj = Parallel(n_jobs=-1, backend="threading")
my_squares = parrallel_obj(delayed(slow_square)(n) for n in nums_to_square)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print()

print("----- CPU BOUND -----")
print("Standard")
start_time = time.time()
for n in primes:
    is_prime(n)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print()

print("Joblib Loky Execution")
start_time = time.time()
parrallel_obj = Parallel(n_jobs=-1, backend="loky")
my_primes = parrallel_obj(delayed(is_prime)(n) for n in primes)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print()

print("Joblib Threaded Execution")
start_time = time.time()
parrallel_obj = Parallel(n_jobs=-1, backend="threading")
my_primes = parrallel_obj(delayed(is_prime)(n) for n in primes)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")