#!/usr/bin/python

import RPi.GPIO as GPIO
import time

import flowmeter


GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)


fm = flowmeter.FlowMeter('metric', 'beer')
fm.enabled = True


def doAClick(channel):
  currentTime = int(time.time() * flowmeter.FlowMeter.MS_IN_A_SECOND)
  if fm.enabled == True:
    fm.update(currentTime)


GPIO.add_event_detect(23, GPIO.RISING, callback=doAClick, bouncetime=20)


while True:
  currentTime = int(time.time() * flowmeter.FlowMeter.MS_IN_A_SECOND)

  print 'current pour: %s || total pour: %s' % (fm.thisPour, fm.totalPour)

  if (fm.thisPour > 0.01 and currentTime - fm.lastClick > 1000): # 1 seconds of inactivity causes a print msg
    msg = "Someone just blew %s of %s with a total breath of %s.\n" % (fm.getFormattedThisPour(), fm.getBeverage(), fm.getFormattedTotalPour())
    fm.thisPour = 0.0
    print msg

