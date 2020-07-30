#all position are relative to homing positions
#all axis are wrt to homing position
#x- parallel to the rails that connect end to end
#y- perp to x
#z- to ground

steps_stepper = 32 #define stepper steps here
gearratio_stepper = 64 #define gear ratio here 
speed_constant = 0.1 #change this to change overall stepper speed
step_constant = 0.1 # this is an experimental value to be determined for unit distance find constant
step_value = steps_stepper * gearratio_stepper * speed_constant #the step value the motor takes
step_distance = step_value * step_constant # the distance the motor will make the load move on one step

x_max_distance = step_distance * 100 #the maximux x distance the plotter can go (the second is the constant which controls the distance is experimental value)
y_max_distance = step_distance * 20 #the maximux x distance the plotter can go (the second is the constant which controls the distance is experimental value)
z_max_distance = step_distance * 50 #the maximux x distance the plotter can go (the second is the constant which controls the distance is experimental value)

currentpos_stepper = [0,0,0] #this determines where the robot is now,ie the robot gripper


sign = lambda x: (1, -1)[x<0] #can be called as function returns sign of the parameter

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
	 #change the values from cartesian distance to steps
	x_reach_insteps = (x - currentpos_stepper[0]) / step_constant
	y_reach_insteps = (y - currentpos_stepper[1]) / step_constant
	z_reach_insteps = (z - currentpos_stepper[2]) / step_constant

	#save the variable to another variable so that the original variable may not get corrupted
	currentservopos = currentpos_stepper[0]

	#we can multithread this block to increase speed if we want to.

	#do a for loop from current step to step required with steps having sign - or positive and update the currentpos_stepper variable too
	for x in range(currentservopos[0],x_reach_insteps,sign(x_reach_insteps-currentservopos[0]) * step_value):
		xaxis_steppermotor(sign(x_reach_insteps-currentservopos[0]) * step_value)
		currentpos_stepper[0] += sign(x_reach_insteps-currentservopos[0]) * step_distance

	if not (currentpos_stepper[0] - x) == 0 : xaxis_steppermotor(sign(currentpos_stepper[0] - x) * (currentpos_stepper[0] - x) / step_constant) #goto extra distance if the for function had some remainder

		#do a for loop from current step to step required with steps having sign - or positive and update the currentpos_stepper variable too
	for y in range(currentservopos[1],y_reach_insteps,sign(y_reach_insteps-currentservopos[1]) * step_value):
		xaxis_steppermotor(sign(y_reach_insteps-currentservopos[1]) * step_value)
		currentpos_stepper[1] += sign(y_reach_insteps-currentservopos[1]) * step_distance

	if not (currentpos_stepper[1] - y) == 0 : xaxis_steppermotor(sign(currentpos_stepper[1] - y) * (currentpos_stepper[1] - y) / step_constant) #goto extra distance if the for function had some remainder

		#do a for loop from current step to step required with steps having sign - or positive and update the currentpos_stepper variable too
	for z in range(currentservopos[2],z_reach_insteps,sign(z_reach_insteps-currentservopos[2]) * step_value):
		xaxis_steppermotor(sign(z_reach_insteps-currentservopos[2]) * step_value)
		currentpos_stepper[2] += sign(z_reach_insteps-currentservopos[2]) * step_distance

	if not (currentpos_stepper[2] - z) == 0 : xaxis_steppermotor(sign(currentpos_stepper[2] - z) * (currentpos_stepper[2] - z) / step_constant) #goto extra distance if the for function had some remainder


	#so what we did here was get the positions to go to substract it from currentposition then we get cartesian distance which is divided by step constant
	#to get the step value to be fed into the motor then we run a for loop such starting from currentpos to the new position updating the positions in each step.

	pass


def findpickbox_recognize():
	#we have to find the box by identifying the borders of tape

	pass


def main():
	if !checkifhomed():
		homeall_steppermotors()


	gotoposition_steppermotor(x,y,x)




if __name__ == 'main':
	main()




