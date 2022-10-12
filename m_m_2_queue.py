import csv
import pandas as pd
import datetime as dt

end_time = [0,0]

pattern1 = pd.read_csv("path.csv")
with open("path.csv",encoding="utf_8") as f:
    reader = csv.reader(f)
    line=[row for row in reader]

for i in range(len(pattern1)):
    aa1 = line[i+1][0].replace(":"," ").split()
    print(int(aa1[1])+int(aa1[0])*60)
    
    counter_no, mi = 0, end_time[0]
    for j, e in enumerate( end_time[1:], 1 ):
        if mi > e:
            counter_no, mi = j, e
