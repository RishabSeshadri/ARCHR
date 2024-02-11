
import asyncio
from bleak import BleakScanner
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            devices = await BleakScanner.discover()

            for d in devices:
                url = f"http://34.138.254.116:80/isValid/{d.address}"

                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data:
                            print("[Address:", d.address, "; Card number: ", data, "]")
                        
            await asyncio.sleep(1)

asyncio.run(main())
