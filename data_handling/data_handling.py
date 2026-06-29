import csv
import matplotlib.pyplot as plt

from datetime import datetime

file_csv = 'data_handling/sitka_weather_07-2018_simple.csv'
with open(file_csv) as file_object:
    data = list(csv.reader(file_object))
    # print(reader[0][1])
    

# for no,item in enumerate(data[0]):
#     print(f'{no} : {item}')
   

TMAX , TMIN , DATE = [],[],[]

for row in data[1:] :
    date_ = datetime.strptime(row[2], '%Y-%m-%d') 
    DATE.append(date_)
    max_ = int(row[5])
    TMAX.append(max_)
    min_ = int(row[6])
    TMIN.append(min_)
    
    
# --- GRAPHING SECTION ---

# 1. Choose a clean visual style for your chart
plt.style.use('seaborn-v0_8')

# 2. Create the figure window and axis
fig, ax = plt.subplots()

# 3. Plot the TMAX list as a solid red line
ax.plot(DATE, TMAX, c='red', linewidth=2)
ax.plot(DATE, TMIN, c='blue', linewidth=2)
ax.fill_between(DATE, TMAX, TMIN, facecolor='blue', alpha=0.1)
# 4. Set titles and labels for your chart
fig.autofmt_xdate()
ax.set_title("Daily High and low Temperatures - Sitka (July 2018)", fontsize=18)
ax.set_xlabel("Days of the Month", fontsize=12 ,)
ax.set_ylabel("Temperature (F)", fontsize=12)

# 5. Pop up the graph window on your screen
plt.show()


