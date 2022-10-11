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
    