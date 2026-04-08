import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/User_experience"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

wiki_text = " ".join([p.text for p in paragraphs])

print("Length:", len(wiki_text))
print(wiki_text[:1000])