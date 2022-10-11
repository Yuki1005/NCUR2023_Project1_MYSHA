import csv
end_time = [0,0]
rows = []
with open("") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

print(rows)