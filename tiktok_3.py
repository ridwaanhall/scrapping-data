import requests
from bs4 import BeautifulSoup

user_title_input = input("Enter TikTok username : ")
url = "https://www.tiktok.com/@" + user_title_input

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print("Avatar    :", soup.find('div',{'data-e2e': 'user-avatar'}).find('img', {})['src'] if soup.find('div',{'data-e2e': 'user-avatar'} ) else "")
print("Title     :", soup.find('h2', {'data-e2e' : 'user-title'}).text         if soup.find('h2', {'data-e2e' : 'user-title'}) else "")
print("Subtitle  :", soup.find('h1', {'data-e2e' : 'user-subtitle'}).text      if soup.find('h1', {'data-e2e' : 'user-subtitle'}) else "")
print("Followers :", soup.find('strong', {'data-e2e': 'following-count'}).text if soup.find('strong', {'data-e2e': 'following-count'}) else "")
print("Following :", soup.find('strong', {'data-e2e': 'followers-count'}).text if soup.find('strong', {'data-e2e': 'followers-count'}) else "")
print("Likes     :", soup.find('strong', {'data-e2e': 'likes-count'}).text     if soup.find('strong', {'data-e2e': 'likes-count'}) else "")
print("Bio       :", soup.find('h2', {'data-e2e': 'user-bio'}).text            if soup.find('h2', {'data-e2e': 'user-bio'}) else "")
print("Link      :", soup.find('a', {'data-e2e': 'user-link'})['href']         if soup.find('a', {'data-e2e': 'user-link'}) else "")
