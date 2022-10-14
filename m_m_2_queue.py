import csv
import pandas as pd
import networkx as nx
import math


end_time = [0,0]
end_time2 = [0,0]
G = nx.read_weighted_edgelist("dijkstra.txt",create_using=nx.DiGraph) 

pattern1 = pd.read_csv("path.csv")
with open("path.csv",encoding="utf_8") as f:
    reader = csv.reader(f)
    line=[row for row in reader]

for i in range(len(pattern1)):
    aa1 = line[i+1][0].replace(":"," ").split()
    arrival_time = int(aa1[1])*60+int(aa1[0])*3600
    
    if line[i+1][2] in ["53","54","55","56","57","58"]:
        aaa = str("I" + line[i+1][2])
    else:
        aaa = str("D" + line[i+1][2])
    
    counter_no, mi = 0, end_time[0]
    for j, e in enumerate( end_time[1:], 1 ):
        if mi > e:
            counter_no, mi = j, e
    
    if counter_no == 0:
        bbb = "X"
    else:
        bbb = "S"
    
    if aaa == "D100":
        print(line[i+1][0],line[i+1][1],"欠航")
    else:
        start_time = arrival_time if arrival_time > end_time[counter_no] else end_time[counter_no]
        end_time[counter_no] = start_time + int(nx.dijkstra_path_length(G,aaa,bbb))/5.55
        interval = end_time[counter_no] - end_time2[counter_no]
        
        if interval < 240:
            end_time[counter_no] = end_time2[counter_no] + 240
        else:
            end_time[counter_no] = end_time[counter_no]
        
        aida = 
        big_hand = str(int(end_time[counter_no])//3600)
        little_hand = str(math.ceil(int(end_time[counter_no])%3600/60) + 3)
        end_time2[counter_no] = end_time[counter_no]
        
        if len(little_hand) == 1:
            runway = big_hand + ":0" + little_hand
        else:
            runway = big_hand + ":" + little_hand
        
        print( '{}  {}  Gate[{}] Runway[{}] 滑走路到着時間{} {}'\
            .format(line[i+1][0],line[i+1][1],aaa, bbb,runway,) )