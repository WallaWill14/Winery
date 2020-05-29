# barrelCalc.py
# Cole Meyers
# Will Thompson
# 28 May 2020
#
# This program calculates volume of liquid inside a tank from a dip measurement.

# Dependencies
###################################################################################
from JPLGui_Engine import *
import math

# Constants
###################################################################################


# Create array of tank names to reuse in the dropdown menu and output spreadsheet
tanks = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 
		'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22']

# Tank dimension table (gallons/inch, total height, extra gallons)
tank_specs = [ \
	[22, 110, 0], \
	[13.1, 79, 25], \
	[10.3, 78.5, 20], \
	[10.3, 79, 20], \
	[9.24, 59, 15], \
	[6.6, 78.5, 10], \
	[6.47, 78.5, 0], \
	[6.89, 59, 10], \
	[4.45, 59.5, 0], \
	[3.51, 50, 0], \
]


# Functions
###################################################################################


def galToL(gal):
	# Converts gallons to liters
	L = gal * 3.78541
	return L

def runCalc():
	# calculates volume of a tank based on dip measurement entered in input box

	# get current tank number selected by user in dropdown menu
	tank = gui.getWidget('Tank').value()

	# get dip measurement entered by user in input box
	dip = gui.getWidget('Dip (inches)').value()

	# calculates liquid volume in specified tank based on the chart Will provided 28 May 2020
	# NOTE: some of the formulas overlap, hence there are less than 22 if/elifs below
	if tank == 'T1':
		gal = tank_specs[0][0] * (tank_specs[0][1] - float(dip))
	elif tank == 'T1' or tank == 'T2' or tank == 'T3' or tank == 'T4' or tank == 'T5':
		gal = (tank_specs[1][0] * (tank_specs[1][1] - float(dip))) + tank_specs[1][2]
	elif tank == 'T6' or tank == 'T7' or tank == 'T8':
		gal = (tank_specs[2][0] * (tank_specs[2][1] - float(dip))) + tank_specs[2][2]
	elif tank == 'T9':
		gal = (tank_specs[3][0] * (tank_specs[3][1] - float(dip))) + tank_specs[3][2]
	elif tank == 'T10' or tank == 'T11' or tank == 'T12':
		gal = (tank_specs[4][0] * (tank_specs[4][1] - float(dip))) + tank_specs[4][2]
	elif tank == 'T13' or tank == 'T14' or tank == 'T17':
		gal = (tank_specs[5][0] * (tank_specs[5][1] - float(dip))) + tank_specs[5][2]
	elif tank == 'T15' or tank == 'T16':
		gal = (tank_specs[6][0] * (tank_specs[6][1] - float(dip))) + tank_specs[6][2]
	elif tank == 'T18':
		gal = (tank_specs[7][0] * (tank_specs[7][1] - float(dip))) + tank_specs[7][2]
	elif tank == 'T19' or tank == 'T20' or tank == 'T21':
		gal = (tank_specs[8][0] * (tank_specs[8][1] - float(dip))) + tank_specs[8][2]
	elif tank == 'T22':
		gal = (tank_specs[9][0] * (tank_specs[9][1] - float(dip))) + tank_specs[9][2]
	else:
		pass

	# convert gallons to liters to populate the second indicator box
	L = galToL(gal)

	# update gallons box
	gui.updateIndicator('Volume (gal)',round(gal, 2))

	# update liters box
	gui.updateIndicator('Volume (L)',round(L,2))


# GUI creation
###################################################################################

# Create master GUI object
gui = JPLGui('Tank Volume Calculator')

# create a "group", i.e. box the following objects until endGroup()
gui.startGroup('Tank Volume Calculator')

# Add dropdown menu to select tank
gui.addComboBox('Tank',tanks)
gui.endCol()

# add user entry box for dip in inches
gui.addInputBox('Dip (inches)',default='0')
gui.endCol()

# add indicators for calculated volume in gallons and liters
gui.addIndicator('Volume (gal)')
gui.addIndicator('Volume (L)')
gui.endCol()
gui.endRow()
# add button to run calculation after tank and dip are entered
gui.addButton('Calculate',runCalc, horizontalAlign=True)

# space out the buttons
gui.endCol()
gui.endRow()

# close the group, i.e. put a box around the previous objects
gui.endGroup()

# launch GUI!
gui.launch()