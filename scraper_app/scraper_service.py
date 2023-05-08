import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from .sms_service import send_sms


def scraper_func():
    options = Options()
    options.add_argument('--headless') # run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    url = 'https://tashkent.hh.uz/search/vacancy?&area=97&employment=full&employment=part&employment=probation&experience=between1And3&text=NAME%3A%28python+OR+django%29&no_magic=true&L_save_area=true&search_period=30&items_on_page=50'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all('a', {'class': 'serp-item__title', 'data-qa': 'serp-item__title'})
    # companies = soup.find_all('a', {'class': "bloko-link bloko-link_kind-tertiary", "data-qa":"vacancy-serp__vacancy-employer"})

    s = "" 
    for t in titles:
        s += f"{t.text}\n"
    
    # send_sms(f"{jobs}\n{url}") # currently not working due to negative balance
    
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/vacancies.txt", "w") as f:
        f.write(f"Total for today: {len(titles)}\n{s}")

    driver.quit()