"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

URL="https://books.toscrape.com/"
START_PAGE= "catalogue/page-1.html"
TOTAL_COUNT= 10
IMAGE_DIR="images"

def scrap_page(url,remaining):
    try:
        response=requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to scrape\n {e}")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    books= []
    for link in soup.select("article.product_pod"):
        if len(books)>= remaining:
            break
        title_tag=link.select_one("h3 >a")
        title= title_tag.get_text()
        # title= link.h3.a['title']
        image=link.select_one("a > img").get("src")
        # relative_img = link.find('img')['src']
        img_url = urljoin(URL, image)
        print(f"image url - {img_url}")
        filename= sanitize_filename(title) + ".jpg"

        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath - {filepath}")

        print(f"Downloading: {title}")
        download_image(img_url,filepath)
        books.append({"title": title, "image_link":img_url, "filepath": filepath})


    next_link=soup.select_one("li.next > a").get("href")
    next_url= urljoin(url, next_link) if next_link else None
    print(f"All {TOTAL_COUNT} books covers downloaded to images/")
    return books,next_url

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(image, filename):
    try:
        resoponse= requests.get(image, stream=True, timeout=10)
        resoponse.raise_for_status()
        with open(filename, 'wb' ) as f:
            for chunk in resoponse.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")

def main():
    print("Scrapping title and image link")
    current_link = urljoin(URL, START_PAGE)
    collected= []
    while len(collected)< TOTAL_COUNT and current_link:
        remaining = TOTAL_COUNT-len(collected)
        books,next_url= scrap_page(current_link,remaining)
        collected.extend(books)
        current_link= next_url



if __name__ == "__main__":
    main()