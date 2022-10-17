import csv
import pandas as pd
import networkx as nx
import math

data = []
end_time = [0,0]
end_time2 = [0,0]
wait_time_heikin = 0
G = nx.read_weighted_edgelist("dijkstra.txt",create_using=nx.DiGraph) 

pattern1 = pd.read_csv("take_off.csv")
with open("take_off.csv",encoding="utf_8") as f:
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
        print(line[i+1][0],"",line[i+1][1],"","欠航")
        data.append([str(line[i+1][0]),"",str(line[i+1][1]),"","欠航"])
    else:
        jikan = int(nx.dijkstra_path_length(G,aaa,bbb))/5.55 + 180
        start_time = arrival_time
        end_time[counter_no] = int(start_time) + jikan
        interval = end_time[counter_no] - end_time2[counter_no]
        
        if interval < 120:
            end_time[counter_no] = end_time2[counter_no] + 120
        else:
            end_time[counter_no] = end_time[counter_no]
        
        wait_time = (end_time[counter_no] - jikan -start_time)/60
        big_hand = (int(end_time[counter_no]))//3600
        little_hand = math.ceil(int(end_time[counter_no])%3600/60)
        if little_hand >= 60:
            big_hand += 1
            little_hand = little_hand -60
        if len(str(little_hand)) == 1:
            runway = str(big_hand) + ":0" + str(little_hand)
        else:
            runway = str(big_hand) + ":" + str(little_hand)

        end_time2[counter_no] = end_time[counter_no]
        wait_time_heikin += wait_time
        
        go_test = (arrival_time +(math.ceil(wait_time)*60))
        if len(str(math.ceil(int(go_test)%3600/60))) == 1:
            go_time = str(go_test//3600) + ":0" + str(math.ceil(int(go_test)%3600/60))
        else:
            go_time = str(go_test//3600) + ":" + str(math.ceil(int(go_test)%3600/60))


        data.append([str(line[i+1][0]),str(go_time),str(line[i+1][1]),"",str(aaa),str(bbb),runway,str(math.ceil(wait_time))])
        
        print( '{} {} {} {} {} {} {}'\
            .format(str(line[i+1][0]),str(go_time),str(line[i+1][1]),str(aaa),str(bbb),runway,str(math.ceil(wait_time))))

data.append([])
data.append(["平均遅延時間",wait_time_heikin/(i+1)*60,"[s]"])
df_list = pd.DataFrame(data, columns=["定刻","出発時間","行先","","ゲート番号","滑走路","滑走路到着時間","遅延"])
df_list.to_csv("m_m_2.csv", index=False,encoding="shift_jis")
print("平均遅延時間",wait_time_heikin/(i+1)*60,"[s]")


#CSV出力方法、たきこちゃん
#パワポ作成
#風向きに合わせたもの kazamuki[1or0] if文で x s h an に