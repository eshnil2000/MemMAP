# Define the number of lines to generate
num_lines = 100000
outfile='../data/m_1_1M.out'
infile='../data/output.csv'

# Read the lines from output.csv
with open(infile, 'r') as f:
    lines = f.readlines()

# Open the output file for writing
with open(outfile, 'w') as f:
    # Repeat the lines and write them to the output file
    for _ in range(num_lines):
        for line in lines:
            f.write(line)

print(f"{num_lines*10} lines have been generated and saved to mext_1_1M.out")
