import csv
import pandas as pd
import networkx as nx
import math

data = []
end_time = [0, 0]
end_time2 = [0, 0]
l = 0
takeoff = 0
arrive = 0
kazamuki = 0
wait_time_heikin = 0
wait_time_takeoff = 0
wait_time_arrive = 0

kankaku = 60

G = nx.read_weighted_edgelist("dijkstra_data.txt", create_using=nx.DiGraph)
pattern1 = pd.read_csv("project_code_final1_data.csv")

def nakami():
    global end_time
    global end_time2
    global wait_time_heikin
    global wait_time_takeoff
    global wait_time_arrive
    global l
    global takeoff
    global arrive
    
    if len(str(line[i+1][2])) == 0:
            start_time = arrival_time
            end_time[counter_no] = start_time
            interval = end_time[counter_no] - end_time2[counter_no]
            
            if interval < kankaku:
                    end_time[counter_no] = end_time2[counter_no] + kankaku
            else:
                end_time[counter_no] = end_time[counter_no]
            big_hand = int(end_time[counter_no]//3600)
            little_hand = math.ceil(end_time[counter_no] % 3600/60)
            if little_hand >= 60:
                big_hand += 1
                little_hand = little_hand - 60
            if len(str(little_hand)) == 1:
                runway = str(big_hand) + ":0" + str(little_hand)
            else:
                runway = str(big_hand) + ":" + str(little_hand)
            end_time2[counter_no] = end_time[counter_no]
            wait_time = (end_time[counter_no] - arrival_time)/60
            
            data.append([str(line[i+1][0]), "", str(line[i+1][1]), "", "着陸",str(bbbb),str(runway),str(math.ceil(wait_time))])
            print(str(line[i+1][0]), "", str(line[i+1][1]), "", "着陸",str(bbbb),str(runway),str(math.ceil(wait_time)))
            wait_time_heikin += wait_time
            wait_time_arrive += wait_time
            l += 1
            arrive += 1
            
            
    else:
        if line[i+1][2] in ["53", "54", "55", "56", "57", "58"]:
            aaa = str("I" + line[i+1][2])
        else:
            aaa = str("D" + line[i+1][2])

        if aaa == "D100":
            print(line[i+1][0],"",line[i+1][1],"","欠航")
            data.append([str(line[i+1][0]),"",str(line[i+1][1]),"","欠航"])
                
        else:
            jikan = int(nx.dijkstra_path_length(G,aaa,bbb))/5.55 + 120
            start_time = arrival_time
            end_time[counter_no] = start_time + jikan
            interval = end_time[counter_no] - end_time2[counter_no]
                
            if interval < kankaku:
                end_time[counter_no] = end_time2[counter_no] + kankaku
            else:
                end_time[counter_no] = end_time[counter_no]
                
            wait_time = (end_time[counter_no] - jikan -start_time)/60
            big_hand = int((end_time[counter_no])//3600)
            little_hand = math.ceil(end_time[counter_no]%3600/60)
            if little_hand >= 60:
                big_hand += 1
                little_hand = little_hand -60
            if len(str(little_hand)) == 1:
                runway = str(big_hand) + ":0" + str(little_hand)
            else:
                runway = str(big_hand) + ":" + str(little_hand)

            end_time2[counter_no] = end_time[counter_no]
            wait_time_heikin += wait_time
            wait_time_takeoff += wait_time
                
            go_test = (arrival_time +(math.ceil(wait_time)*60))
            if len(str(math.ceil(int(go_test)%3600/60))) == 1:
                go_time = str(go_test//3600) + ":0" + str(math.ceil(int(go_test)%3600/60))
            else:
                go_time = str(go_test//3600) + ":" + str(math.ceil(int(go_test)%3600/60))
            l += 1
            takeoff += 1


            data.append([str(line[i+1][0]),str(go_time),str(line[i+1][1]),"",str(aaa),str(bbbb),runway,str(math.ceil(wait_time))])
            print( '{} {} {} {} {} {} {}'\
                .format(str(line[i+1][0]),str(go_time),str(line[i+1][1]),str(aaa),str(bbbb),runway,str(math.ceil(wait_time))))


with open("project_code_final1_data.csv", encoding="utf_8") as f:
    reader = csv.reader(f)
    line = [row for row in reader]

for i in range(len(pattern1)):
    aa1 = line[i+1][0].replace(":", " ").split()
    arrival_time = int(aa1[1])*60+int(aa1[0])*3600
    
    counter_no, mi = 0, end_time[0]
    for j, e in enumerate(end_time[1:], 1):
        if mi > e:
            counter_no, mi = j, e
        
    if int(len(line[i+1][3])) > 0:
        kazamuki += 1
        end_time[0] += 180
        end_time[1] += 180
        end_time2[0] += 180
        end_time2[1] += 180
        
    if kazamuki%2 == 1:
        if counter_no == 0:
            bbb = "S"
            bbbb = "16L"
        else:
            bbb = "X"
            bbbb = "16R"
        nakami()
        
    elif kazamuki%2 == 0:
        if counter_no == 0:
            bbb = "I"
            bbbb = "34R"
        else:
            bbb = "AN"
            bbbb = "34L"
        nakami()

data.append([])
data.append(["平均遅延時間","", wait_time_heikin/l*60, "[s]"])
data.append(["平均出発遅延時間","", wait_time_takeoff/takeoff*60, "[s]"])
data.append(["平均到着遅延時間","", wait_time_arrive/arrive*60, "[s]"])
df_list = pd.DataFrame(
    data, columns=["定刻", "出発時間", "行先","","ゲート番号", "滑走路", "滑走路到着時間", "遅延"])
df_list.to_csv("project_code_final1.csv", index=False, encoding="shift_jis")
print("平均遅延時間", wait_time_heikin/l*60, "[s]")
print("平均出発遅延時間", wait_time_takeoff/takeoff*60, "[s]")
print("平均到着遅延時間", wait_time_arrive/arrive*60, "[s]")


data = []
with open("project_code_final1.csv", encoding="shift_jis") as f:
    reader = csv.reader(f)
    line = [row for row in reader]

pattern1 = pd.read_csv("project_code_final1.csv")
for i in range(len(pattern1)):
    if len(line[i+1][1]) == 0:
        if len(line[i+1][6]) > 0:
            data.append([line[i+1][6],line[i+1][4],line[i+1][5]])
    else:
        data.append([line[i+1][1],line[i+1][4],line[i+1][5]])
        
df_list = pd.DataFrame(data,columns=["時間","飛行機","滑走路"])
df_list.to_csv("project_code_final1_jikokuhyo.csv", index=False, encoding="shift_jis")


#csvを国際、国内線に分ける
#一秒に何分進むかを検討する
#playcanvasを入れてもらってtextの表示の仕方を実際に試してもらう
#行先が同じ機体をリストアップしてもらう
#コードのフローチャート




#離陸の平均速度は220km/h