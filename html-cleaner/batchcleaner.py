from bs4 import BeautifulSoup
import codecs
import os

# Input directory path
input_directory = 'html_inputs'

# Output directory path
output_directory = 'output_txt_files'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to clean text
def clean_text(text):
    # Remove unnecessary spaces and join lines with spaces
    line_split =  ' '.join(line.strip() for line in text.splitlines() if line.strip())
    return ''.join([char for char in line_split if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"“”‘’\''])


# Function to process HTML file
def process_html_file(input_file_path, input_directory, output_directory):
    with codecs.open(input_file_path, 'r', 'utf-8') as html_file:
        # Parse the HTML content
        soup = BeautifulSoup(html_file, 'html.parser')

        # Extract text from the parsed HTML
        text_content = soup.get_text()

        # Clean the text
        cleaned_text = clean_text(text_content)

        # Construct the relative output file path with a .txt extension
        relative_path = os.path.relpath(input_file_path, input_directory)
        output_file_path = os.path.join(output_directory, relative_path)
        output_file_path = os.path.splitext(output_file_path)[0] + '.txt'

        # Create the output directory for the current file if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Save the cleaned text to the output file
        with codecs.open(output_file_path, 'w', 'utf-8') as text_file:
            text_file.write(cleaned_text)

# Traverse the input directory and its subdirectories
for root, dirs, files in os.walk(input_directory):
    for file_name in files:
        if file_name.endswith('.html'):
            # Construct the full input file path
            input_file_path = os.path.join(root, file_name)

            # Process the HTML file and save the cleaned text to the output file with a .txt extension
            process_html_file(input_file_path, input_directory, output_directory)

            print(f"Processed {input_file_path} and saved to {output_directory}")

print("All HTML files processed, and cleaned text saved to the output directory with .txt extension.")
