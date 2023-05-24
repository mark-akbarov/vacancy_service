import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def djinni_scraper():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument('--headless') # run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    url = 'https://djinni.co/jobs/?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=Python&exp_level=no_exp&exp_level=1y&exp_level=2y&page=1'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    titles = soup.find_all('div', class_ = 'list-jobs__title list__title order-1')
    titles = [t.text.strip().replace('\n', '') for t in titles]

    company_divs = soup.find_all('div', class_ = 'list-jobs__details__info')
    companies = [i.find('a').text.strip() for i in company_divs]

    job = {"website_name": "Djinni", "datetime": datetime.date.today(), "job_list": []}

    for _id, (company, title) in enumerate(zip(companies, titles)):
        job_dict = {}
        job_dict['id'] = _id
        job_dict['company'] = company
        job_dict['title'] = title
        job['job_list'].append(job_dict)

    driver.quit()

    return job
