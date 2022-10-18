import csv
import pandas as pd

data = []
with open("queue_final_a1.csv", encoding="shift_jis") as f:
    reader = csv.reader(f)
    line = [row for row in reader]

pattern1 = pd.read_csv("queue_final_data.csv")
for i in range(len(pattern1)):
    if len(line[i+1][1]) == 0:
        if len(line[i+1][6]) > 0:
            data.append([line[i+1][6],line[i+1][4],line[i+1][5]])
    else:
        data.append([line[i+1][1],line[i+1][4],line[i+1][5]])
        
df_list = pd.DataFrame(data,columns=["時間","飛行機","滑走路"])
df_list.to_csv("jikokuhyo1.csv", index=False, encoding="shift_jis")