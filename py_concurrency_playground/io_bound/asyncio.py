'''
Why the asyncio Version Rocks
It’s really fast!
The execution timing diagram looks quite similar to what’s happening in the threading example.
It’s just that the I/O requests are all done by the same thread

The Problems With the asyncio Version
You need special async versions of libraries to gain the full advantage of asyncio.
Another, more subtle, issue is that all of the advantages of cooperative multitasking 
get thrown away if one of the tasks doesn’t cooperate. A minor mistake in code can 
cause a task to run off and hold the processor for a long time, starving other tasks that 
need running. There is no way for the event loop to break in if a task does not hand control 
back to it.
'''
import asyncio

import aiohttp


async def download_site(session, url, debug=False):
    async with session.get(url) as response:
        if debug:
            print(f'Read {response.content_length} from {url}')


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
