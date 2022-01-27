import bindings

from digi.xbee.devices import Raw802Device, RemoteRaw802Device, XBee64BitAddress
from .MessageTypes import MessageTypes

BAUD_RATE = 9_600
DRONE_ADDR = XBee64BitAddress.from_hex_string('0013A20041BAD281')
GROUND_ADDR = XBee64BitAddress.from_hex_string('0013A20041BAD278')

class Telemetry:
    @staticmethod
    def recept_data(msg):
        data = msg.data.decode('ascii')
        bindings.recept_data(data)

    def __init__(self, port, context):
        # Local device configuration
        self.local = Raw802Device(port, BAUD_RATE)
        self.local.open()
        self.local.add_data_received_callback(Telemetry.recept_data)
        # Remote device configuration
        if context not in ('ground', 'drone'):
            bindings.throw_exception('Unknown context')
        remote_addr = DRONE_ADDR if context == 'ground' else GROUND_ADDR
        self.remote = RemoteRaw802Device(self.local, x64bit_addr=remote_addr)
    
    def send_cmd(self, data):
        try:
            MessageTypes[data.split(' ')[0]]
        except KeyError:
            bindings.throw_exception('Unknown command')
        self.local.send_data_async(self.remote, data)