import csv
with open("LST2024_Zonal_Sta.csv", encoding="utf-8-sig") as f:
     reader = csv.DictReader(f)
     rows = list(reader)
     print("Number of rows:", len(rows))
     print( "Columns:", list(rows[0].keys()))
import csv
with open("LST2026_Zonal_Sta.csv", encoding="utf-8-sig") as f:
     reader = csv.DictReader(f)
     rows = list(reader)
     print("Number of rows:", len(rows))
     print("Columns:", list(rows[0].keys()))

import csv
with open("LST2024_zonal_Sta.csv", encoding="utf-8-sig") as f:
     rows = list(csv.DictReader(f))

values = []
for row in rows:
     value = float (row["_mean"])
     values.append(value)

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))    

import csv
with open("LST2026_Zonal_Sta.csv", encoding="utf-8-sig") as f:
     rows = list(csv.DictReader(f))

values = []
for row in rows:
     value = float (row["_mean"])
     values.append(value)

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))    

import csv
with open("LST2024_zonal_Sta.csv", encoding="utf-8-sig") as f:
     rows = list(csv.DictReader(f))
values = []
for row in rows:
     raw = row["_mean"].strip()
     if raw == "":
          continue
     values.append(float(raw))

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv
with open("LST2026_Zonal_Sta.csv", encoding="utf-8-sig") as f:
     rows = list(csv.DictReader(f))
values = []
for row in rows:
     raw = row["_mean"].strip()
     if raw == "":
          continue
     values.append(float(raw))

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
          rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
           continue
        values.append(float(raw))
    return {
         "smallest": min(values),
         "largest": max(values),
         "count": len(values),
    }    

result = inspect_column("LST2024_zonal_Sta.csv", "_mean")
print(result)

import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
          rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
           continue
        values.append(float(raw))
    return {
         "smallest": min(values),
         "largest": max(values),
         "count": len(values),
    }    

result = inspect_column("LST2026_Zonal_Sta.csv", "_mean")
print(result)

area_result = inspect_column("LST2024_zonal_Sta.csv", "AreaSQKM")
_count_result = inspect_column("LST2024_zonal_Sta.csv", "_count")

print("Area (sq km) Stats:", area_result)
print("Pixel Count Stats:", _count_result)

area_result = inspect_column("LST2026_Zonal_Sta.csv", "AreaSQKM")
_count_result = inspect_column("LST2026_Zonal_Sta.csv", "_count")

print("Area (sq km) Stats:", area_result)
print("Pixel Count Stats:", _count_result)
