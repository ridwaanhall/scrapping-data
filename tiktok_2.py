import requests
from bs4 import BeautifulSoup

user_title_input = input("Enter TikTok username : ")
url = "https://www.tiktok.com/@" + user_title_input

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

user_avatar     = soup.find('div',{'data-e2e': 'user-avatar'}).find('img', {})['src'] if soup.find('div',{'data-e2e' : 'user-avatar'}) else ""
user_title      = soup.find('h2', {'data-e2e' : 'user-title'}).text         if soup.find('h2', {'data-e2e' : 'user-title'}) else ""
user_subtitle   = soup.find('h1', {'data-e2e' : 'user-subtitle'}).text      if soup.find('h1', {'data-e2e' : 'user-subtitle'}) else ""
following_count = soup.find('strong', {'data-e2e': 'following-count'}).text if soup.find('strong', {'data-e2e': 'following-count'}) else ""
followers_count = soup.find('strong', {'data-e2e': 'followers-count'}).text if soup.find('strong', {'data-e2e': 'followers-count'}) else ""
likes_count     = soup.find('strong', {'data-e2e': 'likes-count'}).text     if soup.find('strong', {'data-e2e': 'likes-count'}) else ""
user_bio        = soup.find('h2', {'data-e2e': 'user-bio'}).text            if soup.find('h2', {'data-e2e': 'user-bio'}) else ""
user_link       = soup.find('a', {'data-e2e': 'user-link'})['href']         if soup.find('a', {'data-e2e': 'user-link'}) else ""

print("Avatar    :", user_avatar)
print("Title     :", user_title)
print("Subtitle  :", user_subtitle)
print("Followers :", followers_count)
print("Following :", following_count)
print("Likes     :", likes_count)
print("Bio       :", user_bio)
print("Link      :", user_link)
