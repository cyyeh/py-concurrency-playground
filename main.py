import asyncio
import time

from py_concurrency_playground import io_bound, cpu_bound

if __name__ == '__main__':
    print('I/O bound example...\n')
    sites = [
        'https://www.jython.org',
        'http://olympus.realpython.org/dice',
    ] * 80

    print('[naive version]: Start downloading sites...')
    start_time = time.time()
    io_bound.naive.download_all_sites(sites)
    duration = time.time() - start_time
    # [naive version]: Downloaded 160 in 25.59972906112671 seconds
    print(f'[naive version]: Download {len(sites)} sites in {duration} seconds\n')

    print('[threading version]: Start downloading sites...')
    start_time = time.time()
    max_workers = 30
    io_bound.threading.download_all_sites(sites, max_workers=max_workers)
    duration = time.time() - start_time
    # [threading version]: Download 160 in 1.6044700145721436 seconds with maximum 30 workers
    print(f'[threading version]: Download {len(sites)} sites in {duration} seconds with maximum {max_workers} workers\n')

    print('[asyncio version]: Start downloading sites...')
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(
        io_bound.asyncio.download_all_sites(sites)
    )
    duration = time.time() - start_time
    # [asyncio version]: Download 160 sites in 1.6472792625427246 seconds
    print(f'[asyncio version]: Download {len(sites)} sites in {duration} seconds\n')

    print('[multiprocessing version]: Start downloading sites....')
    start_time = time.time()
    io_bound.multiprocessing.download_all_sites(sites)
    duration = time.time() - start_time
    # [multiprocessing version]: Download 160 sites in 4.265676975250244 seconds
    print(f'[multiprocessing version]: Download {len(sites)} sites in {duration} seconds\n')

    print('CPU bound example...')
    numbers = [5000000 + x for x in range(20)]

    print('[naive version]: Start processing...')
    start_time = time.time()
    cpu_bound.naive.find_sums(numbers)
    duration = time.time() - start_time
    # [naive version]: Processing took 7.683359861373901 seconds
    print(f'[naive version]: Processing took {duration} seconds\n')

    print('[threading version]: Start processing...')
    start_time = time.time()
    max_workers = 30
    cpu_bound.threading.find_sums(numbers, max_workers=max_workers)
    duration = time.time() - start_time
    # [threading version]: Processing took 8.008002996444702 seconds with maximum 30 workers
    print(f'[threading version]: Processing took {duration} seconds with maximum {max_workers} workers\n')

    print('[multiprocessing version]: Start processing...')
    start_time = time.time()
    cpu_bound.multiprocessing.find_sums(numbers)
    duration = time.time() - start_time
    # [multiprocessing version]: Processing took 2.6922080516815186 seconds
    print(f'[multiprocessing version]: Processing took {duration} seconds\n')
