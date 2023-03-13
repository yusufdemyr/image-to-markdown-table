import pandas as pd
# Convert the Markdown table to a list of lists
with open('table.md') as f:
    rows = []
    for row in f.readlines():
        
        # Get rid of leading and trailing '|'
        tmp = row[1:-2]
        # Split line and ignore column whitespace
        clean_line = [col.strip() for col in tmp.split('|')]
        # Append clean row data to rows variable
        rows.append(clean_line)
    # Get rid of syntactical sugar to indicate header (2nd row)
    rows = rows[:1] + rows[2:]
print(rows)
df = pd.DataFrame(rows)
df.to_csv('my_file.csv', index=False, header=False)