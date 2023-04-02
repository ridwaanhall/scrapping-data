import requests
import urllib.parse
from bs4 import BeautifulSoup

UTI = input("Enter TikTok username : ")
url = "https://www.tiktok.com/@" + UTI

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

UA  = soup.find('div'   , {'data-e2e' : 'user-avatar'})
UT  = soup.find('h2'    , {'data-e2e' : 'user-title'})
US  = soup.find('h1'    , {'data-e2e' : 'user-subtitle'})
FIC = soup.find('strong', {'data-e2e' : 'following-count'})
FEC = soup.find('strong', {'data-e2e' : 'followers-count'})
LC  = soup.find('strong', {'data-e2e' : 'likes-count'})
UB  = soup.find('h2'    , {'data-e2e' : 'user-bio'})
UL  = soup.find('a'     , {'data-e2e' : 'user-link'})

split_url   = UL['href'].split('target=')
encoded_url = split_url[1]
decoded_url = urllib.parse.unquote(encoded_url)

print("Avatar    :", UA.find('img', {})['src'] if UA  else "")
print("Title     :", UT.text    if UT  else "")
print("Subtitle  :", US.text    if US  else "")
print("Followers :", FIC.text   if FIC else "")
print("Following :", FEC.text   if FEC else "")
print("Likes     :", LC.text    if LC  else "")
print("Bio       :", UB.text    if UB  else "")
print("Link      :", UL['href'] if UL  else "")
print("LinkDecode:", decoded_url)