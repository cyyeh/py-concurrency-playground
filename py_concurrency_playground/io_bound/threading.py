'''
Why the threading Version Rocks
It uses multiple threads to have multiple open requests out to web sites at the same time, 
allowing your program to overlap the waiting times and get the final result faster!

The Problems with the threading Version
Well, as you can see from the example, it takes a little more code to make this happen, 
and you really have to give some thought to what data is shared between threads.
Threads can interact in ways that are subtle and hard to detect. 
These interactions can cause race conditions that frequently result in random, intermittent bugs 
that can be quite difficult to find.
'''
import concurrent.futures
import threading

import requests


# thread local storage
# threading.local() creates an object that looks like a global 
# but is specific to each individual thread.
thread_local = threading.local()


def get_session():
    # requests.Session() is not thread-safe
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url, debug=False):
    session = get_session()
    with session.get(url) as response:
        if debug:
            print(f'Read {len(response.content)} from {url}')


def download_all_sites(sites, max_workers=10):
    # The difficult answer here is that the correct number of threads is not a constant 
    # from one task to another. Some experimentation is required.
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_site, sites)
