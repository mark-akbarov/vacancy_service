from django.shortcuts import render
from .hh_task import hh_scraper
from .djinni_task import djinni_scraper


def index(request):
    hh = hh_scraper()
    djinni = djinni_scraper()
    context = {"hh": hh, "djinni": djinni}
    return render(request, "scraper_app/base.html", context)
