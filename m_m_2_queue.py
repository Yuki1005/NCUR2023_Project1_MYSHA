import pandas as pd
end_time = [0,0]
pattern1 = pd.read_csv("path.csv",usecols=["Time","Go","Gate"])
for i in range(len(pattern1)):
    print(pattern1[1])