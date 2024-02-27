import requests
from bs4 import BeautifulSoup
from weasyprint import HTML

# Get the HTML content of the target webpage
url = "https://www.example.com"
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the desired content from the webpage
title = soup.find("title").text
body = soup.find("body")

# Create the HTML content for the PDF file
pdf_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: sans-serif;
        }}
    </style>
</head>
<body>
    {body}
</body>
</html>
"""

# Convert the HTML content to a PDF file
html = HTML(string=pdf_html)
pdf = html.write_pdf()

# Save the PDF file to disk
with open("output.pdf", "wb") as f:
    f.write(pdf)

print("PDF file created successfully!")
