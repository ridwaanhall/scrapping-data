import requests
from bs4 import BeautifulSoup

user_title_input = input("Enter TikTok username : ")
url = "https://www.tiktok.com/@" + user_title_input

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

user_avatar     = soup.find('div',{'data-e2e': 'user-avatar'}).find('img', {})['src']
user_title      = soup.find('h2', {'data-e2e' : 'user-title'}).text
user_subtitle   = soup.find('h1', {'data-e2e' : 'user-subtitle'}).text
following_count = soup.find('strong', {'data-e2e': 'following-count'}).text
followers_count = soup.find('strong', {'data-e2e': 'followers-count'}).text
likes_count     = soup.find('strong', {'data-e2e': 'likes-count'}).text
user_bio        = soup.find('h2', {'data-e2e': 'user-bio'}).text
user_link       = soup.find('a', {'data-e2e': 'user-link'})['href']

print("Avatar    :", user_avatar)
print("Title     :", user_title)
print("Subtitle  :", user_subtitle)
print("Followers :", followers_count)
print("Following :", following_count)
print("Likes     :", likes_count)
print("Bio       :", user_bio)
print("Link      :", user_link)
