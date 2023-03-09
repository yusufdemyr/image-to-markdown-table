# Open and read the file
with open('data.txt', 'r') as f:
    data = f.read()

# Split each line into a list
rows = [row.split() for row in data.split('\n')]

# Table headers
headers = rows[0]

# Initialize the Markdown table
table = '| ' + ' | '.join(headers) + ' |\n' + '| ' + ' | '.join(['---' for _ in headers]) + ' |\n'

# Add each row to the table
for row in rows[1:]:
    table += '| ' + ' | '.join(row) + ' |\n'

# Save the table to a text file
with open('table1.md', 'w') as f:
    f.write(table)
