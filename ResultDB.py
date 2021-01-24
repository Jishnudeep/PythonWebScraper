import requests
from bs4 import BeautifulSoup

URL = 'https://result.smuexam.in/ex23.php?eid=NOVEMBER/DECEMBER%20SEMESTER%20EXAMINATION%202020'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='portfolio')

print(results.prettify())