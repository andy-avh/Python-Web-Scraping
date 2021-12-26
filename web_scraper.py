from urllib.request import urlopen
import re # to work with regular expressions
from bs4 import BeautifulSoup # tool for parsing out HTML pages

url = "http://olympus.realpython.org/profiles/dionysus"
# ^ website we want to scrape ^
page = urlopen(url)# Open web page

# Extract HTML from desired page - returning as a sequence of bytes
html_bytes = page.read()
html = html_bytes.decode("utf-8") # Decode the bytes to a string

#print(html) - test to print html content

### Using BeautifulSoup ###
soup = BeautifulSoup(html, "html.parser") # assign BeautifulSoup object to variable soup
print(soup.get_text()) # print the text
#  use find_all() to return a list of all instances of that particular tag

image1, image2 = soup.find_all("img") # returns a list of all <img> tags in HTML document
# print(image1["src"]) # get the source of the images




### Extract Text From HTML With String Methods ###
# Title
'''
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
'''
# Problem with this ^^ is it often includes html alongside the string (which we don't want)


### Extract Text From HTML With Regular Expressions ###
'''
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
'''


