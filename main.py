import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open('Brightest Stars.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset_1.append(i)

with open('Dwarf Stars.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset_2.append(i)

planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]

planet_data = []
for index, row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index])

for index1, row1 in enumerate(planet_data_2):
    planet_data.append(planet_data_2[index1])

with open('Final.csv', 'a+')as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(dataset_1[0])
    csv_writer.writerows(planet_data)