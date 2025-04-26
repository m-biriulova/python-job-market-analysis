from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

SEARCH_KEYWORD = "Python"
OUTPUT_FILE = "jobs_filtered.xlsx"

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)

try:
    search_url = f"https://www.jobs.cz/prace/?q={SEARCH_KEYWORD.lower()}"
    driver.get(search_url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "SearchResultCard"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    jobs = []
    listings = soup.find_all("article", class_="SearchResultCard")

    for listing in listings:
        title_tag = listing.find("h2", class_="SearchResultCard__title")
        footer_items = listing.find_all("li", class_="SearchResultCard__footerItem")
        link_tag = listing.find("a", href=True)

        if not (title_tag and link_tag):
            continue

        title = title_tag.get_text(strip=True)
        company = footer_items[0].get_text(strip=True) if len(footer_items) > 0 else ""
        location = footer_items[1].get_text(strip=True) if len(footer_items) > 1 else ""
        link = link_tag["href"]
        if link.startswith("/"):
            link = "https://www.jobs.cz" + link

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Link": link
        })


    if jobs:
        df = pd.DataFrame(jobs)
        df.to_excel(OUTPUT_FILE, index=False)
    else:
        print("[DEBUG] No vacancies found file not created.")

except Exception as e:
    print(f"[ERROR] An error occurred: {e}")
    html = driver.page_source
    with open("debug_page.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML-file debug_page.html for analysis.")

finally:
    driver.quit()
