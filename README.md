# Aibo-Cognex
The server is the aibo. The client is the cognex camera.

the camera message is formatted as such:
aibo_x_pos aibo_y_pos aibo_orientation x_target_pos y_target_pos

the aibo decides to move based on the following decision tree:
targetVector = [x_target_pos, y_target_pos]
aiboVector = [aibo_x_pos,aibo_y_pos,aibo_orientation]

xDif = targetVector[0] - aiboVector[0]
yDif = targetVector[1] - aiboVector[1]

target_angle = tan(yDif/xDif)

#a function of target_angle and aibo_orientation decides to turn left or right.
#it will turn in discrete steps.

#after the angle is within some threshold, it move fowards towards the target.

#if the orientiation leaves the threshold, the controller will readjust orientation as before.

