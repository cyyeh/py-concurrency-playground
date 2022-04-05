'''
Why the multiprocessing Version Rocks
The multiprocessing version of this example is great because 
it’s relatively easy to set up and requires little extra code. 
It also takes full advantage of the CPU power in your computer.

The Problems With the multiprocessing Version
This version of the example does require some extra setup, 
and the global session object is strange. 
You have to spend some time thinking about which variables will be accessed in each process.
'''
import multiprocessing

import requests


session = None

# each process has its own memory space, the global for each one will be different.
def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url, debug=False):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        if debug:
            print(f'{name}: Read {len(response.content)} from {url}')


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)
