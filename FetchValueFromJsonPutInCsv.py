import json
import csv

json_file_path = "/home/rajat/code/ops_lookup/data.json"
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
volume_ids = [volume['VolumeId'] for volume in data['Volumes']]
csv_file_path = 'volume_ids.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['VolumeId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for volume_id in volume_ids:
        writer.writerow({'VolumeId': volume_id})
print(f'VolumeIds have been extracted and stored in {csv_file_path}')
