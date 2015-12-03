import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime
import pir
'''
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = golb.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1-slave'
'''
# Methods
def main():
  # Board setup    
  gpio.setmode(gpio.BOARD)
  # the Pins
  pirPin = 16
  pirLight = 18
  trigL = 38
  echoL = 36
  trigR = 37
  echoR = 35
  # Pin Setup
  gpio.setup(pirPin, gpio.IN)
  gpio.setup(pirLight, gpio.OUT)
  while True:
    program(pirPin, pirLight, trigL, echoL, trigR, echoR)

def program(pirPin, pirLight, trigL, echoL, trigR, echoR):
  threading.Timer(1, pir.getPir(pirPin, pirLight)).start()
  outDist = getDist(trigL, echoL)
  print (outDist)
  time.sleep(1)
  inDist = getDist(trigR, echoR)
  print (inDist)

#def getTemp():

def getDist(TRIG, ECHO):
    #This is a pre written method which checks an ultrasonic sensor that is connected to the pi
    #So the pins will be imported depending which sensor is running in the while loop further down
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    gpio.output(TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.2)
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO)==0:
      pulse_start = time.time()
    while gpio.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print ("Distance: " + str(distance) + "cm")
    return distance

main()

gpio.cleanup()
sys.exit()