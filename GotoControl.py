#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
dronekit-sitl copter
mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551

© Copyright 2015-2016, 3D Robotics.
simple_goto.py: GUIDED mode "simple goto" example (Copter Only)

Demonstrates how to arm and takeoff in Copter and how to navigate to points using Vehicle.simple_goto.

Full documentation is provided at http://python.dronekit.io/examples/simple_goto.html
"""

from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
import DataStore
import thread

# Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


# Start SITL if no connection string specified
# if not connection_string:
#     import dronekit_sitl
#     sitl = dronekit_sitl.start_default()
#     connection_string = sitl.connection_string()

connection_string = "udp:127.0.0.1:14551"  #SImulation
#connection_string = "tcp:192.168.4.1:23"  #ESP

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
# vehicle = connect(connection_string, wait_ready=True)
vehicle = connect(connection_string, wait_ready=False)

DataStore.vehicle = vehicle
import DroneLogic


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    # while not vehicle.is_armable:
    #     print(" Waiting for vehicle to initialise...")
    #     time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    count = 0
    while not vehicle.armed:
        print(" Waiting for arming...")
        count = count +1
        if count > 10:
            return
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    # while True:
    #     print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    #     # Break and return from function just below target altitude.
    #     if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
    #         print("Reached target altitude")
    #         break
    #     time.sleep(1)


#arm_and_takeoff(10)

print("Set default/target airspeed to 3")
vehicle.airspeed = 5

import Server
thread.start_new_thread(Server.run, ())

while True:
    time.sleep(10)