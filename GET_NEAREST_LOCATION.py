#######
#import the required packages
#######

import mysql.connector as myDBConnect
import tkinter as tk  
from functools import partial 
import math

root = tk.Tk() 

##### connect to the database
conn = myDBConnect.connect(user='root', password='Abhi@1214', host='127.0.0.1',port=3306,database = "MAP")

##### initialie a cursor
##### get the row entries in list format
mycursor = conn.cursor()
mycursor.execute("SELECT * FROM locations")
myresult = mycursor.fetchall()
point1=[]
for row in myresult:
    location_x=row[1]
    location_y=row[2]
    location_id=row[0]
    vehicle_Loc=[location_x,location_y,location_id]
    point1.append(vehicle_Loc)
def takeSecond(elem):
    return elem[1]

##### calculate the distance between the coordinates using the EUCLIDEAN DISTANCE
distances = []
def get_Location_ID(X,Y):
    my_coords=[X,Y]
    for entry in point1:
        vehicle_coords = []
        vehicle_coords=[entry[0],entry[1]]
        vehicle_dis_ID =[]
        vehicle_dis_ID=[entry[2],math.floor(math.dist(vehicle_coords, my_coords))]
        distances.append(vehicle_dis_ID)
        distances.sort(key = takeSecond)
    result = distances[:5]
    return result

##### display the result in the label
def call_result(n1, n2):  
    num1 = int(n1.get())  
    num2 = int(n2.get())  
    vehicle_ID =[]
    vehicle_ID = get_Location_ID(num1,num2) 
    string_Output = "Vehicle_ID   Distance(kms)\n"
    for entry in vehicle_ID:
        string_Output += str(entry[0]) + "\t" + str(entry[1])+"\n"
    labelResult.configure(text=string_Output,foreground='blue')  


######
# The GUI for the Front End
######
root.geometry('400x200+100+200')    
root.title('Find Nearest Vehicles')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="Location_X").grid(row=1, column=0)  
labelNum2 = tk.Label(root, text="Location_Y").grid(row=2, column=0)  
  
label = tk.Label(root,text = "Vehicle IDs will be shown here",font=('arial',10,'bold'),foreground='#364156')   
label.grid(row=7, column=2)  
labelResult = tk.Label(root)   
labelResult.grid(row=10, column=2)  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, number1, number2)  
buttonCal = tk.Button(root, text="Find the vehicles", command=call_result).grid(row=3, column=0)  
root.mainloop()  