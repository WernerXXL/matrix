import paho.mqtt.client as mqtt
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from PIL import ImageFont

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90)

font = ImageFont.load_default()

def on_message(client, userdata, msg):
    text = msg.payload.decode()
    with canvas(device) as draw:
        draw.text((0, 0), text, fill="white", font=font)

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("matrix/display")
client.on_message = on_message
client.loop_forever()
