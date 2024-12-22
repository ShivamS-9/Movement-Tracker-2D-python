# taking S = (0,0) on the coordinate system

import math
import numpy as np
import matplotlib.pyplot as plt
print("Welcome to the program.")
given_list = []

def curr_location(x, y):
    if x == 0 and y == 0:
        print("At S")
    elif x == 0:
        print(f"{ 'North' if y > 0 else 'South' } of S")
    elif y == 0:
        print(f"{ 'East' if x > 0 else 'West' } of S")
    else:
        print(f"{ 'North' if y > 0 else 'South' }-{ 'East' if x > 0 else 'West' } of S")
        
total_distance = 0
def distance_cal(x0,y0,x1,y1):
    global total_distance
    d = round(math.sqrt((x0-x1)**2 +(y0-y1)**2), 2) 
    print("Current distance from S:", d)
    total_distance +=d

while True:
    print("Wanna add more values? Y or N:")
    user_input = input()
    if (user_input.lower() == "n"):
        print("Exiting")
        break
    elif (user_input.lower() == "y"):
        while True:
            print("Enter distance: ")
            distance = input()
            try:
                dis_int = int(distance)
                distance = int(distance)
                break
            except:
                print(f"Value not interger.Re-enter pl\n")
        while True:
            print("Enter direction(N/S/E/W/NE/NW/SE/SW): ")
            direction = input()
            if direction.upper() in ["N", "S", "E", "W", "NE", "NW", "SW", "SE"]:
                new_input = (distance,direction)
                given_list.append(new_input)
                break
            else:
                print("Direction does not exist. Enter again\n")
            

x = [0]
y = [0]
Xfinal =0
Yfinal =0 
project = math.sqrt(1/2)
tempX=0
tempY=0
for dist, direct in given_list:
    match direct:
        case "N":
            tempX = x[-1]
            tempY = y[-1]
            x.append(round(tempX,2))
            y.append(round(dist ,2))  
            Yfinal += dist 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "S":
            tempX = x[-1]
            tempY = y[-1]
            x.append(round(tempX,2))
            y.append(round(-dist,2))
            Yfinal -= dist 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "E":
            tempX = x[-1]
            tempY = y[-1]
            x.append(round(dist ,2))
            y.append(round(tempY,2)) 
            Xfinal += dist 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "W":
            tempX = x[-1]
            tempY = y[-1]
            x.append(round(-dist,2))  
            y.append(round(tempY,2)) 
            Xfinal -= dist 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "NE":
            tempX = x[-1]
            tempY = y[-1]
            d = round(dist * project,2)
            y.append(round(d ,2))
            Yfinal += d 
            x.append(round(d,2))   
            Xfinal += d 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "NW":
            tempX = x[-1]
            tempY = y[-1]
            d = round(dist * project,2)
            y.append(round(d,2))   
            Yfinal += d 
            x.append(round(-d,2))    
            Xfinal -= d 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "SE":
            tempX = x[-1]
            tempY = y[-1]
            d = round(dist * project,2)
            y.append(round(-d ,2)) 
            Yfinal -= d 
            x.append(round(d,2))
            Xfinal += d 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])
        case "SW":
            tempX = x[-1]
            tempY = y[-1]
            d = round(dist * project,2)
            y.append(round(-d,2))   
            Yfinal -= d 
            x.append(round(-d,2))
            Xfinal -= d 
            curr_location(Xfinal,Yfinal)
            distance_cal(tempX,tempY,x[-1],y[-1])


print("X:",x)
print("Y:",y)
print("Final location: ", end=" ")
curr_location(Xfinal,Yfinal)
print("Total distance covered: ", total_distance)
plt.plot(x, y)
plt.scatter(x, y, label='Data Points', color='red', marker='o')
plt.show()

