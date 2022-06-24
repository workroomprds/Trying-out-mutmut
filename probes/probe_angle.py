from src import angle

from random import random
from random import randint
from math import isnan

class generators:
  def randomWholeHour():
    return(randint(0,24))

  def randomWholeMinute():
    return(randint(0,60))

  def randomFloat(max):
    return(max*random())

  def randomFloat1K():
    return(generators.randomFloat(1000))

  def randomFloat2Kround0():
    return(1000-generators.randomFloat(2000))


def check(hour, minute, result):
  def outOfBounds(val):
    return((val <0) or (val>360))
  def notWhole(val):
    return(int(val) != val)
  def isNaN(val):
    return(isnan(val))
    
  def printOutput(message):
    print(f"{result} from {hour} and {minute} - {message}")
    
  if outOfBounds(result):
    printOutput("Out Of Bounds")
  if notWhole(result): 
    printOutput("Float not int")
  if isNaN(result):
    printOutput("Not a number")

def probe(hour, minute):
  check(hour, minute, angle.between(hour,minute))
  


RUNS = 3
#hourmaker = generators.randomWholeHour
#minutemaker = generators.randomWholeMinute
#hourmaker = generators.randomFloat1K
#minutemaker = generators.randomFloat1K
hourmaker = generators.randomFloat2Kround0
minutemaker = generators.randomFloat2Kround0



for i in range(RUNS):
  probe(hourmaker(), minutemaker())

  # CONCLUSIONS
    # the angles are >360 if the minutes are >60
    # ... the code needs to modulo 60 
    # the angle isn't an int if the hours aren't an int
    # the angle isn't an int if the minutes aren't an int
    # ... the code needs to manage non-int input
    # manages to return +ve wioth - inputs

# THIS FAILS
#probe("zdkjfh", "jk")
  # CONLCUSIONS
    # crashes on strings