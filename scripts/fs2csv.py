import re
import csv

infile='../data/data.txt'
outfile='../data/output.csv'
# Read the data from the file
with open(infile, 'r') as file:
    data = file.readlines()
pattern = r'ts=(\d+)\s+pid=(\d+)\s+inst=(\d+)\s+cpuid=(\d+)\s+rip=([\da-fx]+)\s+va=([\da-fx]+)'

# Prepare the CSV data
csv_data = []
for line in data:
    #match = re.match(r'ts=(\d+) mstress pid=(\d+)  inst=(\d+) cpuid=(\d+) rip=([a-f\d]+) va=([a-f\d]+)', line)
    match = re.match(pattern, line)
    if match:
        ts, pid, inst, cpuid, rip, va = match.groups()
        #csv_data.append([ts, pid, inst, cpuid, rip, '0x'+va])
        #csv_data.append(['0x'+va+":",'R', '0x'+va])
        csv_data.append([va+":",'R', va])

# Write CSV data to a file
with open(outfile, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile,delimiter=" ")
    #csv_writer.writerow(['ts', 'pid', 'inst', 'cpuid', 'rip', 'va'])
    csv_writer.writerows(csv_data)

print("CSV conversion completed.")
