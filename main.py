#all position are relative to homing positions
#all axis are wrt to homing position
#x- parallel to the rails that connect end to end
#y- perp to x
#z- to ground

steps_stepper = 32 #define stepper steps here
gearratio_stepper = 64 #define gear ratio here 
speed_constant = 0.1 #change this to change overall stepper speed
step_constant = 0.1 # this is an experimental value to be determined
step_distance = step_value * step_constant # the distance the motor will make the load move on one step
step_value = steps_stepper * gearratio_stepper * speed_constant #the step value the motor takes

currentpos_stepper = [0,0,0] #this determines where the robot is now,ie the robot gripper


def xaxis_steppermotor(stp):
	#the x position to go to
	pass

def yaxis_steppermotor(stp):
	#the y position to go to
	pass

def zaxis_steppermotor(stp):
	#the z position to go to
	pass

def checkifhomed_steppermotors():
	#check if reed switches are on
	#return boolean array
	pass

def homeall_steppermotors():
	while !checkifhomed_steppermotors(): #exit loop when all servos are in homing position
		xaxis_steppermotor(-step_value)
		yaxis_steppermotor(-step_value)
		zaxis_steppermotor(-step_value)

	#homed all stepper motors

def getcurrentpos_steppermotors():
	#retrieves the curent position of all steppers wrt homing position
	pass

def gotoposition_steppermotor(x,y,z):
	x_reach = x - currentpos_stepper[0]
	y_reach = y - currentpos_stepper[1]
	z_reach = z - currentpos_stepper[2]

	for x in range(1,10):
		pass
	pass


def main():
	if !checkifhomed():
		homeall_steppermotors()

	gotoposition_steppermotor(x,y,x)






