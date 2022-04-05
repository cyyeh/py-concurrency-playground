import concurrent.futures


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers, max_workers=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(cpu_bound, numbers)
