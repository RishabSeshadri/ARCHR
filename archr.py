import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    print(await BleakScanner.find_device_by_address("B0:BE:83:4B:F1:B8"))
    #for d in devices:

        # DC:B5:4F:AB:CC:8C me
        # B0:BE:83:4B:F1:B8 carlos
        # print("[", d.address.strip(), "]")      
            

asyncio.run(main())