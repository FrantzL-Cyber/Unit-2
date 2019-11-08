from microbit import *
import os, music, radio #music is needed for the buzzer to work, OS aids in manipulating files, Radio is used to send and receive signals


#calibrationVal = pin2.read_analog() #the photosensor can be calibrated before or during the cycle (before if continuous beeps and lighting is desired when the package is opened, during if a knowing when the package was opened and closed is important
sleep(1000) #used to creat space betwee the cycles

#with open("travel_data.txt", "a+") as file: #used to append and/or create the file (a+ does not function for micropy)
file = open("travel_data.txt", "w") #opens the travel_data.txt file to write to {referenced: [https://microbit-micropython.readthedocs.io/en/latest/filesystem.html]}


while True:
    calibrationVal = pin2.read_analog() #calibrates the photosensor during the cycle
    
    sleep(5000) #creates a buffer, done after the calibration to lengthen the time between when the reading is taken and compared, also reduces the amount of accelerometer readings to save on memeory
    
    print(accelerometer.get_values()) #prints the values that are then saved in MU on the plotter
    acc = str(accelerometer.get_values())    
    file.write(acc) #writes the accelerometer readings to the travel_data.txt
    
    #radio.send(accelerometer.get_values()) #messed around for sending the values to a remote device, but did not have a receiver to validate functionality
             
    lightVal = pin2.read_analog() #receives a new light value from pin 2
    
    if lightVal < calibrationVal-5: #compares the light values and determines if they are more than 5 units apart
        pin16.write_digital(1) #if they are more than five apart, then the LED connected to pin 16 turns on
        music.play("C3:8") #the buzzer plays the note C3 for a duration of 8
        file.write("opened") #writes opened to the tracking file
    else:
        pin16.write_digital(0) #if the difference is less than 5 then the LED stays off and no other indicator is recorded.

    if accelerometer.get_z() <= -1000: #change of acceleration of 1000 is close to the acceleration due to gravity, therefore it gauges if the package was n freefall
        display.show(Image.SAD) #if it is the face on the screen becomes sad
        file.write("falling") #notes the number of times the package experienced freefall
    else:
        display.show(Image.HAPPY) #if not is stays happy
