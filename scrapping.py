from bs4 import BeautifulSoup
import requests
import pandas as pd


from lxml import html
import sqlite3

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS flaskapi_table(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                quote TEXT, author TEXT)
''')
connect.commit()

def scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

link = 'https://quotes.toscrape.com/'
soup = scrape(link)

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for i in range(len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)

    print()
    cursor.execute("""
                    INSERT INTO flaskapi_table(quote, author) VALUES(?, ?)
    """, (quotes[i].text, authors[i].text))
    connect.commit()