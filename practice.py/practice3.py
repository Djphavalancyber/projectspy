
import requests
from bs4 import BeautifulSoup

# Set the URL for the blog website of The Times of India
url = 'https://timesofindia.indiatimes.com/blogs'

# Make a request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the blog posts on the page
blog_posts = soup.find_all('div', class_='blog-post')

# Loop through the blog posts and print their titles and URLs
for post in blog_posts:
    title = post.find('h2', class_='post-title').text
    url = post.find('a')['href']
    print(title, url)
