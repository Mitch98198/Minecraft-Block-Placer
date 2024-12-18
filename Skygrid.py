

#want to generate a list of pairs of points between all of the spheres, and check to see if they fall within each sphere
#generate a list of all of the points between the 3 spawners (integer values)

#filling list of all points that are suspected to be in between all three spawners spheres
ordered_points = [(x,y,z) for x in range(16, 38+16) for y in range(143-16,155+16)
for z in range(22-16,38+16)]

#list of valid points, checking to confirm if all the points are valid
valid_points = []

#checking through each possible point to see if it lies within each spawner sphere
for points in ordered_points:
    x_coord = points[0]
    y_coord = points[1]
    z_coord = points[2]
    checkVal = 0
    if((x_coord-30)**2+(y_coord-143)**2+(z_coord-38)**2)<16**2:
        checkVal += 1
    if((x_coord-26)**2+(y_coord-147)**2+(z_coord-30)**2)<16**2:
        checkVal += 1
    if((x_coord-38)**2+(y_coord-151)**2+(z_coord-30)**2)<16**2:
        checkVal += 1
    if((x_coord-34)**2+(y_coord-151)**2+(z_coord-22)**2)<16**2:
        checkVal += 1
    if((x_coord-34)**2+(y_coord-155)**2+(z_coord-26)**2)<16**2:
        checkVal += 1
#making sure our potential blocks are OUTSIDE of the 9 radius sphere zone where spawning is prohibited
    if((x_coord-30)**2+(y_coord-143)**2+(z_coord-38)**2)>9**2:
        checkVal += 1
    if((x_coord-26)**2+(y_coord-147)**2+(z_coord-30)**2)>9**2:
        checkVal += 1
    if((x_coord-38)**2+(y_coord-151)**2+(z_coord-30)**2)>9**2:
        checkVal += 1
    if((x_coord-34)**2+(y_coord-151)**2+(z_coord-22)**2)>9**2:
        checkVal += 1
    if((x_coord-34)**2+(y_coord-155)**2+(z_coord-26)**2)>9**2:
        checkVal += 1
    if checkVal > 9:
        valid_points.append((x_coord,y_coord,z_coord))
    checkVal = 0

for point in valid_points:
    print(point)

with open("placeBlocks.txt","w") as file:
    for point in valid_points:
        x_coord = str(point[0])
        y_coord = str(point[1])
        z_coord = str(point[2])
        txt = "/setblock " + x_coord + " " + y_coord + " " + z_coord + " minecraft:stone\n"
        file.write(txt)
