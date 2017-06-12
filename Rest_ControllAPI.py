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

