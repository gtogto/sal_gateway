import pygatt

adapter = pygatt.BGAPIBackend()

try:
    adapter.start()
    device = adapter.connect('50:33:8B:F1:28:57')
    value = device.char_read("0000ffe1-0000-1000-8000-00805f9b34fb")

finally:
    adapter.stop()

