import json
import csv

def csv_to_json(filename):

    with open(filename, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(reader)
        data_json = json.dumps(rows, indent=4)
        return data_json

print(csv_to_json('новые_данные.csv'))

