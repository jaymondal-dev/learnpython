import requests
from bs4 import BeautifulSoup



# Make a request to the Wikipedia page
response = requests.get('https://www.gradesaver.com/wide-sargasso-sea/study-guide/summary-part-1-section-2')

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first heading (h1) element in the page
heading = soup.find('article').text
# Print the heading
print(heading)

index=heading.find("Analysis")
print(index)
print("\n\n\n")
print(heading[:index])
print("\n\n\n")
print(heading[index:])




#with open("test file txt", 'w') as file: file.write(heading)


