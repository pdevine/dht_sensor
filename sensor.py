#!/usr/bin/python

import Adafruit_DHT
import argparse
import json
import sys

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor_map = {
    'dht11': Adafruit_DHT.DHT11,
    'dht22': Adafruit_DHT.DHT22,
    'am2302': Adafruit_DHT.AM2302,
}

def read_sensor(sensor, pin, human=False):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is None and temperature is None:
        print 'Failed to get sensor reading. Try again!'
	sys.exit(1)

    if human:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        data = {
            'humidity': humidity,
            'temperature': temperature,
        }
        print json.dumps(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read sensors from DHT22/DHT11/AM2302')
    parser.add_argument('--sensor', default='dht22', help="Sensor type. One of 'dht11', 'dht22', 'am2302' (default: dht22)")
    parser.add_argument('--pin', default=17, help="Pin for sensor (e.g. 'P8_11' for Beaglebone Black, '17' for Raspberry Pi GPIO17) (default=17)")
    parser.add_argument('--human', action='store_true', help="Output in human readable form.  Default is JSON.")
    args = parser.parse_args()

    if args.sensor not in ['dht11', 'dht22', 'am2302']:
        print "Must specify one of 'dht11', 'dht22', am2302. You specified: %s" % (args.sensor)

    # Attempt to set the pin to an integer for Raspberry Pi GPIO values.
    pin = ''
    try:
        pin = int(args.pin)
    except ValueError:
        pin = args.pin

    read_sensor(sensor_map[args.sensor], pin, args.human)
