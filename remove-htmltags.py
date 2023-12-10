from bs4 import BeautifulSoup
import codecs

# Input HTML file path
html_file_path = 'katha-1.html'

# Output text file path
text_file_path = 'dammapadaya-pitaka/output.txt'

# Read the HTML file (assuming it's UTF-8 encoded)
with codecs.open(html_file_path, 'r', 'utf-8') as html_file:
    # Parse the HTML content
    soup = BeautifulSoup(html_file, 'html.parser')

    # Extract text from the parsed HTML
    text_content = soup.get_text()

    # Remove English letters, double quotes, and single quotes
    cleaned_text = ''.join([char for char in text_content if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"“”‘’\''])

    # Remove extra whitespaces and newline characters
    cleaned_text = ' '.join(cleaned_text.split())

    # Save the cleaned text content to a text file (UTF-8 encoded)
    with codecs.open(text_file_path, 'w', 'utf-8') as text_file:
        text_file.write(cleaned_text)

print(f"HTML tags removed, specified characters removed, and content saved to {text_file_path}")
