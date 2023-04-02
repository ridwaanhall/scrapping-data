# Import necessary modules
import requests
from bs4 import BeautifulSoup

# Prompt user for Instagram username
username = input("Enter Instagram username: ")

# Build URL for user's profile
url = "https://www.instagram.com/{}".format(username)

# Send GET request and retrieve HTML content
response = requests.get(url)
soup     = BeautifulSoup(response.content, "html.parser")

# Extract user information from meta tag in HTML
meta_tag = soup.find("meta", attrs={"name": "description"})
content  = meta_tag.attrs["content"]
info     = content.split(" - ")[0]
followers, following, posts = info.split(", ")
username = content.split("(@")[1].split(")")[0]

# Print user information to console
print("User Information for {}:".format(username))
print("- Followers : {}".format(followers))
print("- Following : {}".format(following))
print("- Posts     : {}".format(posts))
