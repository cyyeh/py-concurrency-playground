'''
Why the Synchronous Version Rocks

The great thing about this version of code is that, well, it’s easy. It was comparatively easy to write and debug. It’s also more straight-forward to think about. There’s only one train of thought running through it, so you can predict what the next step is and how it will behave.

The Problems With the Synchronous Version
The big problem here is that it’s relatively slow compared to the other solutions we’ll provide.
'''
import requests


def download_site(url, session, debug=False):
    with session.get(url) as response:
        if debug:
            print(f'Read {len(response.content)} from {url}')


def download_all_sites(sites):
    # It is possible to simply use get() from requests directly, 
    # but creating a Session object allows requests to do some 
    # fancy networking tricks and really speed things up.
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)
