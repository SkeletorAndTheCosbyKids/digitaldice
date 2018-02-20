# Digital Dice 
# Page 10
# Number of obtuse triangles

import random

REPLICATES = 1000000

obtuse_triangles = 0
Y_LEN= 2

for i in range(0,REPLICATES):

	x_coords = []
	y_coords = []
	
	for x in range(3):
		x_coords.append(random.uniform(0, 1))
		y_coords.append(random.uniform(0, Y_LEN))
	
	# Improbable, but check for non-triangles
	if x_coords[0] == x_coords[1] and x_coords[0]==x_coords[2]:
		print("not a triangle")
	if y_coords[0] == y_coords[1] and y_coords[0]==y_coords[2]:
		print("not a triangle")
	
	#vertices = [(x_coords[0],y_coords[0]),(x_coords[1],y_coords[1]), (x_coords[2],y_coords[2])]
	#print(type(vertices))
	#print(vertices)
	length_1 = ((x_coords[1] - x_coords [0])**2) + ((y_coords[1] - y_coords[0])**2)
	#length_1 = math.sqrt(length_1)

	length_2 = ((x_coords[2] - x_coords [0])**2) + ((y_coords[2] - y_coords[0])**2)
	#length_2 = math.sqrt(length_2)

	length_3 = ((x_coords[2] - x_coords [1])**2) + ((y_coords[2] - y_coords[1])**2)
	#length_3 = math.sqrt(length_3)
	
	cos_A_numerator = length_2 + length_3 - length_1
	cos_B_numerator = length_1 + length_3 - length_2
	cos_C_numerator = length_1 + length_2 - length_3
	#print(x_coords)
	#print(y_coords)
	if cos_A_numerator < 0 or cos_B_numerator < 0 or cos_C_numerator < 0:
		obtuse_triangles +=1

		
prob_obtuse = obtuse_triangles / REPLICATES
print(prob_obtuse)		
#			totalcorrect = totalcorrect + correct
#avg_correct = totalcorrect / REPLICATES
#print(avg_correct)

