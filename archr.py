
import asyncio
from bleak import BleakScanner
import aiohttp
import requests

from flask import Flask, request, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def home():
    if request.method == 'POST':
        deviceName = request.form['deviceName']
        res = await BleakScanner.find_device_by_name(deviceName)
    
        if res != None:
            str = "http://34.138.254.116:80/add/" + res.address + "/" + deviceName
            requests.get(str)
            return f"Successfully added {deviceName}."

        return f"Failed at adding '{deviceName}'. The device was not found."
    else:
        return render_template('bank.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
async def main():
    deviceName = deviceName.strip().replace("’","'")
    res = await BleakScanner.find_device_by_name(deviceName)
    
    if res != None:
        str = "http://34.138.254.116:80/add/" + res.address + "/" + deviceName
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
"""