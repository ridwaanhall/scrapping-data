import requests
from bs4 import BeautifulSoup

user_title_input = input("Enter TikTok username : ")
url = "https://www.tiktok.com/@" + user_title_input

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

UA  = soup.find('div', {'data-e2e' : 'user-avatar'})
UT  = soup.find('h2' , {'data-e2e' : 'user-title'})
US  = soup.find('h1' , {'data-e2e' : 'user-subtitle'})
FIC = soup.find('strong', {'data-e2e': 'following-count'})
FEC = soup.find('strong', {'data-e2e': 'followers-count'})
LC  = soup.find('strong', {'data-e2e': 'likes-count'})
UB  = soup.find('h2', {'data-e2e': 'user-bio'})
UL  = soup.find('a', {'data-e2e': 'user-link'})

user_avatar     = UA.find('img', {})['src'] if UA  else ""
user_title      = UT.text                   if UT  else ""
user_subtitle   = US.text                   if US  else ""
following_count = FIC.text                  if FIC else ""
followers_count = FEC.text                  if FEC else ""
likes_count     = LC.text                   if LC  else ""
user_bio        = UB.text                   if UB  else ""
user_link       = UL['href']                if UL  else ""

print("Avatar    :", user_avatar)
print("Title     :", user_title)
print("Subtitle  :", user_subtitle)
print("Followers :", followers_count)
print("Following :", following_count)
print("Likes     :", likes_count)
print("Bio       :", user_bio)
print("Link      :", user_link)
