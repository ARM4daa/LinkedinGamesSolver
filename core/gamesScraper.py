"""
gamesScraper.py

Automates the scraping of a targeted page on internet

Author : Baptiste FARCY (ARM4da)
Date : June 2026
"""

# -- Importations --
from playwright.sync_api import sync_playwright
from datetime import datetime

# -- Functions --
def scraping(fileToWrite:str, linkToScrap:str, visibleWindow:bool = False, timeout:int = 3000) -> str :

    """
        Collect the HTML content from the 'linkToScrap' URL and write this content into 'fileToWrite' file.

        Args :
            - fileToWrite (str) : Name of the file to stock the page content
            - linkToScrap (str) : URL of the site to scrap
            - visibleWindow (bool) : Able or disable the visible window, "False" by default
            - timeout (int) : Time in milliseconds to wait for the page to load, "3000" by default
        Returns :
            - fileToWrite (str) : Name of the file to stock the page content
    """
    print("Scraping start")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not visibleWindow)
        page = browser.new_page() 

        page.goto(linkToScrap)
        page.wait_for_timeout(timeout)

        with open(fileToWrite, "w") as file:
            date = datetime.now()                           #Optionnal line : To add the date on top of the collecting content
            date = str(date.strftime("%d-%m-%y %H:%M:%S"))  #Optionnal line : To set the date format
            file.write(date + "\n")
            file.write(page.content())

        browser.close()
        print("Scraping done")
    return fileToWrite

    

