import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def hh_scraper():  
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument('--headless') # run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    url = 'https://www.hh.ru/search/vacancy?&area=97&employment=full&employment=part&employment=probation&experience=between1And3&text=NAME%3A%28python+OR+django%29&no_magic=true&L_save_area=true&search_period=30&items_on_page=50'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all('a', class_ = 'serp-item__title')
    titles = [i.text for i in titles]

    companies = soup.find_all('a', class_ = 'bloko-link bloko-link_kind-tertiary')
    companies = [i.text for i in companies]

    job = {"website_name": "HeadHunter", "datetime": datetime.date.today(), "jobs_list": []}

    for _id, (company, title) in enumerate(zip(companies, titles)):
        job_dict = {}
        job_dict['id'] = _id
        job_dict['company'] = company
        job_dict['title'] = title
        job['jobs_list'].append(job_dict)

    driver.quit()
    
    return job
