import pandas as pd
end_time = [0,0]
pattern1 = pd.read_csv("path.csv",usecols=["Time","Go","Gate"])
a1 = pattern1[((pattern1["Time"]))]
for i in range(len(pattern1)):
    print(a1[1])