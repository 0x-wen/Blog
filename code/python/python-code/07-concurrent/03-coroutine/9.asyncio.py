import asyncio

import aiohttp


async def async_fetch_url(session, url):
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
        return await response.text()


async def main():
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for url in ["https://www.baidu.com", "https://www.baidu.com"]:
            tasks.append(asyncio.create_task(async_fetch_url(session, url)))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Error: {result}")
            else:
                print(result)


asyncio.run(main())
