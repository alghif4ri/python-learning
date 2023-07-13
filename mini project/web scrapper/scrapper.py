# These lines import the necessary libraries for the web scraping task.
# The requests library is used to send HTTP requests and retrieve the HTML content of a webpage.
# The BeautifulSoup class from the bs4 (Beautiful Soup) library is used for parsing and navigating the HTML content.
import requests
from bs4 import BeautifulSoup

# Here, we define the function scrape_quotes() to encapsulate the web scraping logic.
def scrape_quotes():
# We set the url variable to the target website's URL.
    url = "http://quotes.toscrape.com"
# Then, we use requests.get() to send an HTTP GET request to the URL and obtain the response.
    response = requests.get(url)
# We pass it to BeautifulSoup along with the "html.parser" parser to create a BeautifulSoup object called soup.
    soup = BeautifulSoup(response.text, "html.parser")
# The response's text attribute contains the HTML content of the webpage.
# This object represents the parsed HTML structure of the webpage, allowing us to navigate and extract information from it.

# In this line, we use soup.find_all() to find all the div elements with the class "quote".
# These elements contain the quotes and author information on the webpage.
# The returned quotes object is a list of BeautifulSoup Tag objects, each representing a quote.
    quotes = soup.find_all("div", class_="quote")

# In this loop, we iterate over each quote found in the quotes list.
    for quote in quotes:
# For each quote, we use quote.find() to search within the quote element itself for specific elements that contain the quote text and author information.
# The text variable is assigned the span element with the class "text" that represents the quote text. We check if text is not None before accessing its .
        text = quote.find("span", class_="text")
        if text is not None:
# text property to avoid an AttributeError. If text exists, we use .text.strip() to extract the text content of the element and remove any leading/trailing whitespace.
            text = text.text.strip()

# Similarly, the author variable is assigned the small element with the class "author" that represents the author information.
        author = quote.find("small", class_="author")
# We apply the same check for None and extract the text content using .text.strip().
        if author is not None:
            author = author.text.strip()
# Finally, if both text and author exist(i.e., they are not None), we print the quote and author information using print().
        if text and author:
            print(f"Quote: {text}")
            print(f"Author: {author}")
            print()

# This line calls the scrape_quotes() function, triggering the execution of the web scraping process.
scrape_quotes()
