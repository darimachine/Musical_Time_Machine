import requests
from bs4 import BeautifulSoup
year = input("What year would you like to travel YYYY-MM-DD\n")
URl = f"https://www.billboard.com/charts/hot-100/{year}/"
response = requests.get(URl)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
musics = soup.find_all("h3",id="title-of-a-story",class_="u-letter-spacing-0021")

top100=[music.text.strip() for music in musics]
top100 = [value for value in top100 if value!="Songwriter(s):" and value!="Producer(s):" and value!="Imprint/Promotion Label:"]
print(top100)