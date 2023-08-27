import random

outfile='../data/mext_1_1M.out'
infile='../data/output.csv'

# Read the sample lines from the input file
with open(infile, 'r') as input_file:
    sample_lines = input_file.readlines()

# Generate 1 million random lines using the sample lines
random_lines = []
for _ in range(1000000):
    random_line = random.choice(sample_lines)
    random_lines.append(random_line)

# Write the random lines to an output file
with open(outfile, 'w') as output_file:
    for line in random_lines:
        output_file.write(line)

print("Generated 1 million random lines.")