
import asyncio
from bleak import BleakScanner
import aiohttp
import asyncio
from bleak import BleakScanner
import requests

async def main():
    while True:
        deviceName = input('Enter device name: ')
        deviceName = deviceName.strip().replace("’","'")
        cardNumber = input('Enter card number (sample): ')
        res = await BleakScanner.find_device_by_name(deviceName)
        
        if res != None:
            str = "http://34.138.254.116:80/add/" + res.address + "/" + cardNumber
            requests.get(str)
            

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
