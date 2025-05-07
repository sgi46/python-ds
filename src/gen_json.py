import csv 
import json

with open("./output_clean.csv", 'r') as file:
    csv_out=csv.reader(file)
    next(csv_out)
    dict = {}
    for item in csv_out:
        table, sql1, sql2, out = item
        dict[table] = out

with open("./table_load_order.json", 'w') as output:
    json.dump(dict, output, indent=4)
    