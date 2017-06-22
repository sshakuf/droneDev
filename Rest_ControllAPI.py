import RestEngine
import DataStore
import DroneLogic

from dronekit import connect, VehicleMode, LocationGlobalRelative
# import GotoControl
vehicle =''

def Initialize():
#    print(GotoControl.vehicle)
    vehicle = DataStore.vehicle
    print(vehicle)


def Get_pins(inProp):
    c =  " pin "
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def Set_pins(inProp, inVal):
   
    if inVal == 1:
        point1 = LocationGlobalRelative(-35.3625960, 149.1652179, 20)
    else:
        point1 = LocationGlobalRelative(-35.3626660, 149.1660333, 20)
        
    
    DataStore.vehicle.simple_goto(point1, groundspeed=10)

    c =  " point  " + str(inVal) 
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def R_pins(args):
    print('in R_pins')
    print (args)
    
    point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
    DataStore.vehicle.simple_goto(point1)

    c ='s'
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def R_mode(args):
    print('in R_pins')
    print (args)

    DataStore.vehicle.mode = VehicleMode(args[0].upper())
    
    c = DataStore.vehicle.mode   
    content = RestEngine.CreateHTML(c.name)
    header = RestEngine.createHeader(content)
    return header, content
    

def getlocation():
    c =""

    # Print location information for `vehicle` in all frames (default printer)
    # c = "<p>" + c +  "Global Location: " +  str(DataStore.vehicle.location.global_frame) + "</p>"
    # c = "<p>" + c +  "Global Location (relative altitude): %s" + str(DataStore.vehicle.location.global_relative_frame) + "</p>"
    # c = "<p>" + c +  "Local Location: %s" + str(DataStore.vehicle.location.local_frame)  + "</p>"   #NED

    # # Print altitudes in the different frames (see class definitions for other available information)
    # c = "<p>" + c +  "Altitude (global frame): %s" + str(DataStore.vehicle.location.global_frame.alt) + "</p>"
    # c = "<p>" + c +  "Altitude (global relative frame): %s" + str(DataStore.vehicle.location.global_relative_frame.alt) + "</p>"
    # c = "<p>" + c +  "Altitude (NED frame): %s" + str(DataStore.vehicle.location.local_frame.down) + "</p>"
    c = str(DataStore.vehicle.location.global_relative_frame)

    return c
    

def R_location(args):
    print('in R_location')
    print (args)

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

def R_takeoff(args):
    print('in R_location')
    print (args)

    DroneLogic.arm_and_takeoff(5)

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

def R_goto(args):
    print('in R_location')
    print (args)

    if len(args)>=2:
        DroneLogic.goto(int(args[0]), int(args[1]))


    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def R_speed(args):
    print('in R_Speed')
    print (args)
    
    DroneLogic.setSpeed(args)

    c = str(DroneLogic.getSpeed())

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

def R_speed(args):
    print('in R_Alt')
    print (args)
    
    DroneLogic.setAlt(args)

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def Set_joystick(channel, val):
    print('Set_joystick ' + str(channel) + ' ' + str(val))
    
    print "Set Ch2 override to 200 (indexing syntax)"
    DataStore.vehicle.channels.overrides[channel] = val

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content
    

def R_joystick(args):
    print('R_joystick')
    print (args)
    
    # Get all original channel values (before override)
    print "Channel values from RC Tx:", DataStore.vehicle.channels

    # Access channels individually
    print "Read channels individually:"
    print " Ch1: %s" % DataStore.vehicle.channels['1']
    print " Ch2: %s" % DataStore.vehicle.channels['2']
    print " Ch3: %s" % DataStore.vehicle.channels['3']
    print " Ch4: %s" % DataStore.vehicle.channels['4']
    print " Ch5: %s" % DataStore.vehicle.channels['5']
    print " Ch6: %s" % DataStore.vehicle.channels['6']
    print " Ch7: %s" % DataStore.vehicle.channels['7']
    print " Ch8: %s" % DataStore.vehicle.channels['8']
    print "Number of channels: %s" % len(DataStore.vehicle.channels)


    # Override channels
    print "\nChannel overrides: %s" % DataStore.vehicle.channels.overrides

    print "Set Ch2 override to 200 (indexing syntax)"
    DataStore.vehicle.channels.overrides['2'] = 200
    print " Channel overrides: %s" % DataStore.vehicle.channels.overrides
    print " Ch2 override: %s" % DataStore.vehicle.channels.overrides['2']

    print "Set Ch3 override to 300 (dictionary syntax)"
    DataStore.vehicle.channels.overrides = {'3':300}
    print " Channel overrides: %s" % DataStore.vehicle.channels.overrides

    print "Set Ch1-Ch8 overrides to 110-810 respectively"
    DataStore.vehicle.channels.overrides = {'1': 1110, '2': 1210,'3': 1310,'4':1800}
    print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    # time.sleep(100)

    # # Clear override by setting channels to None
    # print "\nCancel Ch2 override (indexing syntax)"
    # DataStore.vehicle.channels.overrides['2'] = None
    # print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    # print "Clear Ch3 override (del syntax)"
    # del DataStore.vehicle.channels.overrides['3']
    # print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    # print "Clear Ch5, Ch6 override and set channel 3 to 500 (dictionary syntax)"
    # DataStore.vehicle.channels.overrides = {'5':None, '6':None,'3':500}
    # print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    # print "Clear all overrides"
    # DataStore.vehicle.channels.overrides = {}
    # print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content




def R_joystickclear(args):
    print('R_joystickclear')
    print (args)
    
    # Get all original channel values (before override)
    print "Channel values from RC Tx:", DataStore.vehicle.channels

    # Access channels individually
    print "Read channels individually:"
    print " Ch1: %s" % DataStore.vehicle.channels['1']
    print " Ch2: %s" % DataStore.vehicle.channels['2']
    print " Ch3: %s" % DataStore.vehicle.channels['3']
    print " Ch4: %s" % DataStore.vehicle.channels['4']
    print " Ch5: %s" % DataStore.vehicle.channels['5']
    print " Ch6: %s" % DataStore.vehicle.channels['6']
    print " Ch7: %s" % DataStore.vehicle.channels['7']
    print " Ch8: %s" % DataStore.vehicle.channels['8']
    print "Number of channels: %s" % len(DataStore.vehicle.channels)


    print "Clear all overrides"
    DataStore.vehicle.channels.overrides = {}
    print " Channel overrides: %s" % DataStore.vehicle.channels.overrides 

    c = getlocation()

    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

