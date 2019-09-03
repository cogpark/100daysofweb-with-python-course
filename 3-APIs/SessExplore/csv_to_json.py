import csv
import json

def converter(file):
    with open(file) as csvfile:
        reader=csv.DictReader(csvfile, fieldnames=("sessionID","Page","Hit Timestamp", "Unique Pageviews","nodeID"))
        out = json.dumps([row for row in reader])
        print("File converted")
        new_file_name = input("Save as...?")
        f = open(new_file_name + ".json", 'w+')
        f.write(out)
        print("Saved!")


file = input("File to convert: ")

converter(file)