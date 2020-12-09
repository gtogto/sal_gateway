import asyncio
from bleak import BleakClient

address = "40:2E:71:72:68:4F"
MODEL_NBR_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"

async def run(address):
	async with BleakClient(address) as client:
		model_number = await client.read_gatt_char(MODEL_NBR_UUID)
		print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))


