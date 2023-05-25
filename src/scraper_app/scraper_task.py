import datetime
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup


async def hh_scraper():
    url = 'https://www.hh.ru/search/vacancy?&area=97&employment=full&employment=part&employment=probation&experience=between1And3&text=NAME%3A%28python+OR+django%29&no_magic=true&L_save_area=true&search_period=30&items_on_page=50'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, 'html.parser')
    
    titles = soup.find_all('a', class_='serp-item__title')
    titles = [i.text for i in titles]
    
    companies = soup.find_all('a', class_='bloko-link bloko-link_kind-tertiary')
    companies = [i.text for i in companies]
    
    job = {"website_name": "HeadHunter", "datetime": datetime.date.today(), "jobs_list": []}
    
    for _id, (company, title) in enumerate(zip(companies, titles)):
        job_dict = {}
        job_dict['id'] = _id
        job_dict['company'] = company
        job_dict['title'] = title
        job['jobs_list'].append(job_dict)
    
    return job


async def djinni_scraper():
    url = 'https://djinni.co/jobs/?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=Python&exp_level=no_exp&exp_level=1y&exp_level=2y&page=1'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, 'html.parser')
    
    titles = soup.find_all('div', class_='list-jobs__title list__title order-1')
    titles = [t.text.strip().replace('\n', '') for t in titles]
    
    company_divs = soup.find_all('div', class_='list-jobs__details__info')
    companies = [i.find('a').text.strip() for i in company_divs]
    
    job = {"website_name": "Djinni", "datetime": datetime.date.today(), "jobs_list": []}
    
    for _id, (company, title) in enumerate(zip(companies, titles)):
        job_dict = {}
        job_dict['id'] = _id
        job_dict['company'] = company
        job_dict['title'] = title
        job['jobs_list'].append(job_dict)
    
    return job
