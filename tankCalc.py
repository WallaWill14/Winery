# barrelCalc.py
# Cole Meyers
# Will Thompson
# 28 May 2020
#
# This program calculates volume of liquid inside a tank from a dip measurement.

from JPLGui_Engine import *
import math

def calcT1(dip):
	dip = float(dip)
	height = 10.0
	radius = 3.0
	eff_height = height - dip
	volIn3 = math.pi*eff_height*(radius**2)
	return volIn3

def calcT2(dip):
	height = 20
	radius = 3
	eff_height = height - dip
	volIn3 = math.pi*eff_height*(radius**2)
	return volIn3

def in3ToGal(vol):
	gal = vol / 231
	return gal

def galToL(gal):
	L = gal * 3.78541
	return L

def runCalc(gui):
	tank = gui.getWidget('Tank').value()
	dip = gui.getWidget('Dip (inches)').value()
	if tank == 'T1':
		volIn3 = calcT1(dip)
	elif tank == 'T2':
		volIn3 = calcT2(dip)
	gal = in3ToGal(volIn3)
	L = galToL(gal)
	gui.updateIndicator('Volume (gal)',gal)
	gui.updateIndicator('Volume (L)',L)

# Create master GUI object
gui = JPLGui('Tank Volume Calculator')

# Create array of tank names to reuse in the dropdown menu and output spreadsheet
tanks = ["T1", "T2"]


# create a "group", i.e. box the following objects until endGroup()
#gui.startGroup('Tank Volume Calculator')
gui.startGroup('Tank Volume Calculator')
# Add dropdown menu to select tank
gui.addComboBox('Tank',tanks)
gui.addInputBox('Dip (inches)',default='0')
gui.addIndicator('Volume (gal)')
gui.addIndicator('Volume (L)')
gui.addButton('Calculate',runCalc(gui))
gui.endCol()
gui.endRow()
gui.endGroup()
# end Tank Volume Calculator group
#gui.endGroup(size=[1,2])




gui.launch()