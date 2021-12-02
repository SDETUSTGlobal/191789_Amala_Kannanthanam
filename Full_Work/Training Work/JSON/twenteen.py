#import necessary modules
import csv

reader = csv.DictReader(open("D:/data.csv"))
for raw in reader:
    print(raw)