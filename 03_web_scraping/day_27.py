"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.

"""

import requests
import os
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw,ImageFont


BASE_URL= "https://quotes.toscrape.com/"
OUTPUT= "quotesimages"

def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote_tage=soup.select("div.quote")
    quote_data = []
    for q in quote_tage[:5]:
        quote=q.find("span", class_="text").text.strip("" "")
        author= q.find("small", class_="author").text.strip()

        quote_data.append((quote,author))

    return quote_data

def create_image(quote, author, index):
    width , height = 800, 400
    backround_color= "#000000"
    text_color = "#FFFFFF"
    image=Image.new("RGB", (width, height), backround_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()
    wrapped = textwrap.fill(quote, width=60)
    author_text= f"- {author}"
    y_axis = 60
    draw.text((40,y_axis), wrapped,font=font, fill=text_color)
    y_axis += wrapped.count('\n') * 15 + 40
    draw.text((500, y_axis), author_text,font=font,fill=text_color)

    ## save image
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)
    
    filename = os.path.join(OUTPUT, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✔️ saved: {filename}")


def main():
    quote = fetch_quotes()
    for idx, (quote, author) in enumerate(quote):
        create_image(quote,author,idx)


if __name__== "__main__":
    main()