import requests
from bs4 import BeautifulSoup

print("RUNNING BLOG FILE")

url = "https://www.nngroup.com/articles/definition-user-experience/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

blog_text = " ".join([p.text for p in paragraphs])

print("Length:", len(blog_text))
print(blog_text[:500])