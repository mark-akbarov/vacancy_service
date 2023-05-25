import asyncio
from django.shortcuts import render
from .scraper_task import hh_scraper, djinni_scraper


async def scrape_data():
    tasks = [
        asyncio.create_task(hh_scraper()),
        asyncio.create_task(djinni_scraper()),
    ]
    results = await asyncio.gather(*tasks)
    return results


def index(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    jobs = loop.run_until_complete(scrape_data())
    return render(request, "scraper_app/base.html", context={"jobs": jobs})
