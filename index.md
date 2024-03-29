# Welcome to the Unit 2 reflection page

The primary focus of Unit 2 was to think about the Internet of Things (IoT) and how a device c
ould be developed and intergrated into it. My final project started off as a sensor to implement 
in a safe. Where when the safe door is opened a key would be required or a message would be sent. 
Integrating the last two aspects into the microbit, proved to be too large for the microbit 
capacity when utilizing micropy. So the project transitioned to a package sensor. 

## **Package Sensor**
![Image](Positive.jpg)

As a reusable package sensor, the microbit with photoresistor, allows the tracking of the package's angles, 
if it is dropped, and if it has been opened. Combined into a battery operated single sensor, it allows the 
recipient to track how the package was treated throughout the delivery. Having used some of the individual 
tilt and shock indicators (usually around $3 each), it seemed like a great task for such a small electronic.
The biggest drawback in utilizing the microbit as a sensor came about with how quickly it can create the 
data sets. Finding an appropriate balance where the end data was manageable while not missing any particular 
'event'. The solution came about just by trial and error, just to ensure the sleep cycle did not interfere 
between the speed the photoresistor comparison needs to happen in versus the tilt changes.



### **Accelerometer**
The microbit accelerometer is used to identify the angles at which the microbit has shifted. 
Using this tool one can see if the package has surpassed a designated angle. Unlike a normal 
tilt indicator, utilizing a microbit for this shows for how long the package was kept above 
a certain angle, and if it ever reached angles surpassing the limits of standard tilt indicators.
![Image](Negative.jpg)

### **Data**

![Image](Shaking.jpg)

Even though the microbit offers very little data storage, the data storage simplicity as a CSV 
(comma seperated variables), mean it is easy and quickly integrated into a MySQL database, or 
even analyzed just using Microsoft Excel.

```Code
while True:
    calibrationVal = pin2.read_analog() 
    #calibrates the photosensor during the cycle
    
    sleep(5000) #creates a buffer, done after the calibration to lengthen the time 
    #between when the reading is taken and compared, also reduces the amount of 
    #accelerometer readings to save on memeory
    
    print(accelerometer.get_values()) #prints the values that are then saved in MU on the plotter
    acc = str(accelerometer.get_values())    
    file.write(acc) #writes the accelerometer readings to the travel_data.txt
    
    #radio.send(accelerometer.get_values()) #messed around for sending the values 
    #to a remote device, but did not have a receiver to validate functionality
             
    lightVal = pin2.read_analog() #receives a new light value from pin 2
```
Being able to transmit the readings to another device could greatly improve the viability of the device.
The ability for these devices to transmit the information outside of the package while remaining inside 
could give both the customer and the shipping provider more piece of mind. It would also identify the 
exact point of failure in the packages delivery, so measures could be taken to avoid them. 


To return to my profile page [Click Here](https://frantzl-cyber.github.io/FL_portfolio/).
