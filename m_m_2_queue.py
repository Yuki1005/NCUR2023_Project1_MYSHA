import csv
import pandas as pd
import networkx as nx

aaa = input("スタート地点を入力")
bbb = input("行き先を入力")
aaa = str.upper(aaa)
bbb = str.upper(bbb)
if aaa == bbb:
    bbb = input("スタート地点とは違う、行き先を入力")
    bbb = str.upper(bbb)

end_time = [0,0]
G = nx.read_weighted_edgelist("dijkstra.txt",create_using=nx.DiGraph) 

pattern1 = pd.read_csv("path.csv")
with open("path.csv",encoding="utf_8") as f:
    reader = csv.reader(f)
    line=[row for row in reader]

for i in range(len(pattern1)):
    aa1 = line[i+1][0].replace(":"," ").split()
    arrival_time = int(aa1[1])+int(aa1[0])*60
    
    counter_no, mi = 0, end_time[0]
    for j, e in enumerate( end_time[1:], 1 ):
        if mi > e:
            counter_no, mi = j, e
    
    
    start_time = arrival_time if arrival_time > end_time[counter_no] else end_time[counter_no]
    end_time[counter_no] = start_time + int(nx.dijkstra_path_length(G,aaa,bbb))
    wait_time = start_time - arrival_time
    
    print( '{}  {}  Gate[{}] {} {:<5} {:>2d} {:>4.0f} {:>4.0f}'\
        .format(line[i+1][0],line[i+1][1],line[i+1][2], counter_no+1, i, i, end_time[counter_no], wait_time ) )