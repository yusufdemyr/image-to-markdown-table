from PIL import Image
import pytesseract

class App:
    def __init__(self):
        pass

    def extract(self,item):
        # Extract text from image
        data = pytesseract.image_to_string(Image.open(item), lang='eng')

        # Clean the text by removing unnecessary newlines and spaces
        clean_data = '\n'.join([line.strip() for line in data.split('\n') if line.strip()])

        # Get table headers from user input
        headers_str = input("Enter table headers (separate by comma): ")

        # Convert headers string to a list by splitting at commas
        headers = headers_str.split(',')

        # Get a list of text rows
        rows = clean_data.split('\n')

        # Initialize the Markdown table
        table = '| ' + ' | '.join(headers) + ' |\n' + '| ' + ' | '.join(['---' for _ in headers]) + ' |\n'

        # Add each row to the table
        for i, row in enumerate(rows[1:]):
            table += '| ' + ' | '.join(row.split()) + ' |\n'
        
        return table

    def save(self,table):
        # Save the table to a text file
        with open('table.md', 'w') as f:
            f.write(table)

    def show(self,table):
        print(table)

