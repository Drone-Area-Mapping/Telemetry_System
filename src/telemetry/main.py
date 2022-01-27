import argparse
from time import sleep
from .Telemetry import Telemetry

parser = argparse.ArgumentParser(description='Configuration of the telemetry process')
parser.add_argument('-p', '--port', type=str, nargs=1, required=True, help='Serial port which the XBee module is connected to')
parser.add_argument('-c', '--context', type=str, choices=['ground', 'drone'], required=True, help='Context of the telemetry process')

args = parser.parse_args()
telemetry = Telemetry(args.port[0], args.context)

match args.context:
    case 'ground':
        while True:
            cmd = input()
            telemetry.send_data(cmd)

    case 'drone':
        while True:
            telemetry.send_data('STATUS')
            sleep(2)
