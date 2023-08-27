"""with open("weather_data.csv") as weather_data:
    data= weather_data.readlines()
    print (data)"""

"""import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures=[]
    for row in data:
        if row[1] != "temp":

            temperatures.append(int(row[1]))
    print(temperatures)"""


import pandas
data = pandas.read_csv("weather_data.csv")

#print(type(data))
#print(type(data["temp"]))
data.to_dict()
print(data.to_dict())
"""""
temp_list = (data["temp"].to_list())
print(data["temp"].max())

#Get data in columns
print(data["condition"])
print(data.condition)"""

#Get data in row
"""print(data[data.day=="Monday"])
max = data.temp.max()
print(data[data.temp==data.temp.max()])"""


"""monday = data[data.day == "Monday"]
monday_temp = (monday.temp)
monday_temp_F = monday_temp *9/5 +32
print(monday_temp_F)"""
"""""
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


grey_squirrels = len(data[data["Primary Fur Color"]=="Gray"])
grey_cinnamon = len(data[data["Primary Fur Color"]=="Cinnamon"])
grey_black = len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrels)
print(grey_cinnamon)
print(grey_black)

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, grey_cinnamon, grey_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")
"""""